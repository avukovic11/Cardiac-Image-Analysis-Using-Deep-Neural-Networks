import matplotlib.pyplot as plt
import numpy as np

# Step function definition
def step_function(x):
    return np.where(x >= 0, x, 0.05 * x)


# Data for plotting
x = np.linspace(-5, 5, 100)
y = step_function(x)

# Plotting
plt.figure()
plt.plot(x, y)
plt.xlabel('net')
plt.ylabel('f(net)')
plt.xlim(-5, 5)
plt.ylim(-1.1, 1.1)
plt.xticks(np.arange(-5, 6, 1))
plt.grid(True)

# Saving the plot as an image file
image_path = 'leaky_relu_function_graph.png'
plt.savefig(image_path)

# Display the plot
plt.show()

image_path
