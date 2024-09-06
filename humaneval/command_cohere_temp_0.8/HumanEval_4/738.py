Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block showing the code and a few tests to validate its functionality:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    """
    if not numbers:
        raise ValueError("Input list is empty")
    
    mean = sum(numbers) / len(numbers)
    devations = [abs(num - mean) for num in numbers]
    return sum(devations) / len(numbers)

# Tests
assert mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 1.0

big_numbers = [10**i for i in range(10)]
assert mean_absolute_deviation(big_numbers) > 10

small_numbers = [1./10**i for i in range(10)]
assert mean_absolute_deviation(small_numbers) < 1
``` 

When you run this script, Python will execute the `mean_absolute_deviation` function and print the result of each test to the console. 

You can modify the tests to check different cases, such as a list with only one element, an empty list, or other scenarios you'd like to explore. 

This way, you can see firsthand how the function behaves and verify its output against your expectations.