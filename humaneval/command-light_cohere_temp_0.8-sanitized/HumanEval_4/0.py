from typing import List
def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).
    >>> MAD = average | x - x_mean |
    """
    
    list_mean = [x for x in numbers if type(x) == float and x != 0]
    numbers_mean = sum(list_mean) / len(list_mean)
    return abs(numbers[-1] - numbers_mean)