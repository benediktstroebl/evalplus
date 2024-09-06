from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    # Handling empty input
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculating the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculating the absolute deviation of each number from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Returning the mean absolute deviation
    return sum(absolute_deviations) / len(numbers)