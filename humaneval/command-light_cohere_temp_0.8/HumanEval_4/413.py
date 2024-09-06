Here's a self-contained Python function that calculates and returns the Mean Absolute Deviation (MAD) of a list of numbers:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculate Mean Absolute Deviation around the mean of this dataset 
    from a given list of numbers.
    MAD = sum((x - x - x_mean) for x, x_mean in zip(numbers, numbers.0.mean())) / len(numbers)
    ``` 

The function first uses the `zip` function to create a list of paired numbers where each number in `numbers` is paired with its mean. Then, the `sum` function is used to calculate the sum of absolute differences between each element in the list and the mean of the list.