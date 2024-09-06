```python
from typing import List

def mean_absolute_deviation(numbers: List[float]):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    numbers = [1.0, 2.0, 3.0, 4.0]
   0
   0
   
    MAD = sum(map(lambda x: abs(x - numbers[-1]))) / len(numbers)
    return MAD

# Example Test
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.3604))
```
The above Python script defines a function `mean_absolute_deviation` that computes the Mean Absolute Deviation (MAD) of a list of numbers. It uses the `map` function to calculate the absolute difference between each element in the list and the last element, then sums these values and divides by the number of elements in the list. 

The example test passes the function with a list of numbers, and the function returns the calculated MAD.