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
    # Mean and standard deviation are calculated on the fly.
    from numpy import asarray, mean, std, absolute

    def mean_std_absolute_deviation(numbers: List[float]) -> float:
        try:
            mean_value = mean(numbers)
            std_value = std(numbers)
            from numpy import absolute as abs_val

            return abs_val(numbers - mean_value).tolist()
        except TypeError:
            return []

    numbers += []
    return mean(numbers, axis=0).std()

