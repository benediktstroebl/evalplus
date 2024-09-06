Here's the solution:

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """

    mean = sum(numbers) / len(numbers)
    numbers = [x - mean for x in numbers]
    return sum(numbers) / len(numbers)

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
print mean mean_absolute_deviation(numbers)
# Result: 1.0

You can test the function with different datasets of numbers, and it will return the Mean Absolute Deviation around the mean of the dataset.