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
    if not numbers:
        return float('inf')

    numbers.sort()  # sort the list so that we can calculate MAD efficiently
    center_index = len(numbers) // 2
    x_mean = sum(numbers) / len(numbers)
    x_max = max(numbers)

    deviation = [abs(numbers[i] - x_mean) for i in range(len(numbers))]
    mean_deviation = sum(deviation) / len(deviation)

    if numbers[0] <= x_mean:
        deviation_tail = deviation[0:center_index]
        deviation_head = deviation[center_index:]
        tail_sum = sum(deviation_tail)
        head_sum = sum(deviation_head)
        tail_mean = tail_sum / tail_sum * x_mean
        head_mean = head_sum / head_sum * x_mean
        if x_max < x_mean:
            return tail_mean + head_mean
    return mean_deviation
