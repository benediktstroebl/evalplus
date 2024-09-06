from typing import List
import numpy as np
def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the mean absolute deviation of a list of numbers.
    
    Mean Absolute Deviation measures the average absolute difference between each element and the mean of the list.
    
    Parameters:
        numbers (List[float]): A list of numbers with at least one element.
        
    Returns:
        float: The mean absolute deviation of the input list.
            
    Example:
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))