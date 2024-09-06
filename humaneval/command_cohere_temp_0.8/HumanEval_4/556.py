Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list is empty. Cannot calculate MAD.")

    mean = math.fmean(numbers)
    mad = sum( abs(x - mean) for x in numbers) / len(numbers)
    return mad
```
This script includes a function called `mean_absolute_deviation()` that calculates the mean absolute deviation of a list of numbers. This is a common statistical measure that reflects the average absolute difference between each number in the list and the mean of the list. 

The function follows the following steps:
1. It checks if the input list is empty, throwing a ValueError if true.
2. It calculates the mean of the list using the `math.fmean()` function (this function calculates the mean of the list of floating-point numbers).
3. It computes the MAD using a list comprehension with absolute value conditioning.
4. Finally, it returns the calculated MAD. 

Overall, this is a robust and efficient script that can be used to calculate the mean absolute deviation of a list of numbers in a self-contained manner. 
Here is an example of how to use the function:
```python
test_list = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(test_list))
``` 

This will output:
```
1.0
```