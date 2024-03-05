import matplotlib.pyplot as plt

# Interactive visualization using Matplotlib
def interactive_visualization(x, y):
    plt.plot(x, y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Interactive Visualization")
    plt.show()

# Example usage:
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
interactive_visualization(x, y)
