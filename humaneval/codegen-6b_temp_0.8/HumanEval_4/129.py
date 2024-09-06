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
    # TODO:   Use median instead of mean (see leetcode question #9)
    # https://leetcode.com/problems/maximum-average-subarray-i/discuss/148746/JavaC%2B%2BPython-Mean-absolute-deviation
    # https://leetcode.com/problems/maximum-average-subarray-i/discuss/23737/JavaC%2B%2BPython-Mean-absolute-deviation
    centerpoint = sum(numbers) / len(numbers)
    # TODO:   bubble sort
    # https://leetcode.com/problems/maximum-average-subarray-i/discuss/24210/Java-and-Python-equivalent-solution-O(n)-time-and-O(1)-space
    absolute_deviations = [abs(p - centerpoint)
                           for p in numbers]
    return sum(absolute_deviations) / len(absolute_deviations)

