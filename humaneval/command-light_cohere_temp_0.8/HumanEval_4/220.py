```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation. The average absolute difference between each
    element and the mean (center value).
    
    Input:
    numbers: List[float]
        List of numbers that will be used in the computation
    
    Returns:
    float
        The Mean Absolute Deviation
    """
    mean = sum(numbers)/len(numbers)
    mad = sum((num - mean)**2 for num in numbers) / len(numbers)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)==1.0)  #True
numbers = [1.0,2.0,3.0,4]
print(mean_absolute_deviation(numbers)==0.0)  #True
numbers = [5.5,5.5,5.5]
print(mean_absolute_deviation(numbers)==0.0)  #True

# Test with wrong data
numbers = [1.0,2,3,4]
print(mean_absolute_deviation(numbers)==12.0) == False
```