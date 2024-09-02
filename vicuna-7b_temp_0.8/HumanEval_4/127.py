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

    return sum(abs(numbers[0] - numbers[i]) for i in range(1, len(numbers))) / len(numbers)


if __name__ == '__main__':
    example_list = List([1.0, 2.0, 3.0, 4.0, 5.0])
    example_mad = mean_absolute_deviation(example_list)
    print("Example MAD:", example_mad)