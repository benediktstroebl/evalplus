Here's the solution for your problem:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset
    
    :param numbers: list of floating-point numbers
    :return: Mean Absolute Deviation
    """
    import statistics
    numbers.mean = statistics.mean(numbers)
   return statistics.median_absolute_deviation(numbers - numbers.mean)
   
   return mean
```
This function computes the Mean Absolute Deviation (MAD) metric, which calculates the average absolute difference between each element and the mean of the dataset.

It takes a list of floating-point numbers as input and returns the Mean Absolute Deviation value. 

The function also includes a type hint for the input parameter, using the `List[float]` syntax, which is a standard convention in Python for specifying the types of the elements in the input parameter. 
It also uses the `statistics` module to access the `mean` function for the calculation of the mean of the input dataset.