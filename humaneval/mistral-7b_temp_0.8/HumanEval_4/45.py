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
    # TODO: Write code to solve the above problem.
    # HINT:
    # 1. There are two ways to calculate mean, first calculate the sum of all
    #    numbers in the list and then divide it by the number of elements in
    #    the list, or secondly, calculate the sum of all numbers and divide it
    #    by 2. (Depends on the data structure you choose to store the list)
    # 2. After you've found the mean, loop through the list and subtract each
    #    element with the mean and take the absolute value of that number
    # 3. Then find the average of all the numbers you found in step 2
    pass

