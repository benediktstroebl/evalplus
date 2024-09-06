Here's a self-contained Python function that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset
    
    :param numbers: List[float] - List of numbers 
    :return: float - Mean Absolute Deviation around mean 
    """
    mean = sum(numbers)/len(numbers)
    mad = sum((x-mean) ** 2 for x in numbers) / len(numbers)
    return mad
```
This function takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) around the mean of the dataset.

You can test the function with the following code:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers) )
``` 
This will return the expected value of the Mean Absolute Deviation.