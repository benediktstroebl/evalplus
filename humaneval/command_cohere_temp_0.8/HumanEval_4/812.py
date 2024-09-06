Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    return sum(abs(x - sum(numbers) / len(numbers)) for x in numbers) / len(numbers)
```
```python
# Test the function with a sample list of numbers
sample_numbers = [1.0, 2.0, 3.0, 4.0]
print(f"Mean Absolute Deviation for {sample_numbers}: {mean_absolute_deviation(sample_numbers)}")
```