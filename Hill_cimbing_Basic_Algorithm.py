import random

# Define a mathematical function, for example, f(x, y) = x^2 + y^2
def evaluate_function(x, y):
    return x**2 + y**2

# Generate random coordinates for the current point
current_x = random.randint(-10, 10)  # Replace -10 and 10 with the desired range
current_y = random.randint(-10, 10)

# Evaluate the function at the current point
current_result = evaluate_function(current_x, current_y)

# Print the current point and its evaluation result
print(f"Current Point: ({current_x}, {current_y})")
print(f"Current Evaluation Result: {current_result}")

# Generate a random direction and step size
random_direction_x = random.uniform(-1, 1)
random_direction_y = random.uniform(-1, 1)
step_size = .1  # Adjust the step size according to your needs

# Update the current point based on the random direction and step size
new_x = current_x + (step_size * random_direction_x)
new_y = current_y + (step_size * random_direction_y)

# Evaluate the function at the new point
new_result = evaluate_function(new_x, new_y)

# Print the new point and its evaluation result
print(f"New Point: ({new_x}, {new_y})")
print(f"New Evaluation Result: {new_result}")

# Check if the new point is deeper than the current point
#
if new_result > current_result:
    current_x = new_x
    current_y = new_y
    print("New point is deeper. Updating current point.")
else:
    print("New point is not deeper. Keeping current point.")

# Print the final current point
print(f"Final Current Point: ({current_x}, {current_y})")