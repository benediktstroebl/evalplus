Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    return sum(abs(x - sum(numbers) / len(numbers)) for x in numbers) / len(numbers)
```
```python
# Test the function with a sample list of numbers
sample_numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(sample_numbers))  # Should print: 1.0
```

This function `mean_absolute_deviation` calculates the mean absolute deviation of a list of numbers. It does so by summing up the absolute deviations of each number from the mean in a list, then dividing by the total number of elements to obtain the average.

The test case at the end demonstrates the usage of this function. The output should be 1.0, indicating the mean absolute deviation of the provided sample numbers.