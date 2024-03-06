import math
import random

def ackley_function(x, y):
    term1 = -20 * math.exp(-0.2 * math.sqrt(0.5 * (x**2 + y**2)))
    term2 = -math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
    return term1 + term2 + math.e + 20

def random_start_point():
    return random.uniform(-5, 5), random.uniform(-5, 5)

def iterated_hill_climbing(iterations):
    best_point = random_start_point()
    best_value = ackley_function(*best_point)

    for _ in range(iterations):
        neighbor_x = best_point[0] + random.uniform(-0.5, 0.5)
        neighbor_y = best_point[1] + random.uniform(-0.5, 0.5)
        neighbor_value = ackley_function(neighbor_x, neighbor_y)

        if neighbor_value < best_value:
            best_point = (neighbor_x, neighbor_y)
            best_value = neighbor_value

    return best_point, best_value

# Number of iterations for each run
iterations_per_run = 1000

# Run iterated hill climbing
best_point, best_value = iterated_hill_climbing(iterations_per_run)

print(f"Best point: {best_point} with value: {best_value}")