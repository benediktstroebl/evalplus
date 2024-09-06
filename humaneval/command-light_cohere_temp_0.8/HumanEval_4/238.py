Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculating the Mean Absolute Deviation around the mean of this dataset.
    mean = sum(numbers)/len(numbers)
    mad = sum((x - mean)**2 for x in numbers) ) / len(numbers)
    return mad
```
The `mean_absolute_deviation` function takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of this dataset.

It calculates the mean of the numbers in the list, then, it calculates the sum of squared differences from the mean for each number in the list. The function then returns the sum of squared differences divided by the length of the list.

This function is self-contained, and it can be used to calculate the MAD of any given list of numbers.