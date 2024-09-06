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
    # mean of the data, rounded to one decimal place
    numbers_mean = sum(numbers) / len(numbers)
    numbers_mean = round(numbers_mean, 1)
    b = 0
    # check if the mean is zero; if so, we can use the absolute mean
    # because in this case, |x| is also equal to |x_mean|
    # The 0.00001 is added to prevent the case where absolute mean is zero
    if abs(numbers_mean) < 0.00001:
        numbers_mean = 0.0
    # calculate the absolute difference between each element and mean
    for number in numbers:
        b += abs(number - numbers_mean)
    mad = b / len(numbers)
    return round(mad, 1)

