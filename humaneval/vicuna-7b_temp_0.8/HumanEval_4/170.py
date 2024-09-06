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
    # Normalize the input numbers to have a mean of zero and a standard deviation of one.
    numbers_norm = [number / np.linalg.norm(numbers) for number in numbers]

    # Take the mean of the normalized numbers
    mean = np.mean(numbers_norm)

    # Calculate the standard deviation of the normalized numbers
    sd = np.linalg.norm(numbers_norm - mean)

    # Calculate the mean absolute deviation of the normalized numbers from the mean
    mad = mean_absolute_deviation_from_mean(numbers_norm, mean)

    return mad

