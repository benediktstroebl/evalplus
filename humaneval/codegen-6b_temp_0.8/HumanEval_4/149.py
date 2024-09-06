from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Check that all values are numbers (int or float)
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Non-numbers not supported")
    # Sort all values
    sorted_numbers = sorted(numbers)
    # Calculate all values in each window
    sorted_numbers_as_slices = [sorted_numbers[i:i + 4] for i in range(0, len(sorted_numbers), 4)]
    # Calculate mean of each window
    mean_of_windows = [sum(x) / len(x) for x in sorted_numbers_as_slices]
    # Calculate mean absolute deviation
    mae = sum([abs(x - mean_of_windows[0]) for x in mean_of_windows]) / (len(mean_of_windows) - 1.0)
    return mae

