Here is a self-contained Python script that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Make the list of numbers into a list of (mini, mid, max) values
    min_val, max_val = min(numbers), max(numbers)
    return [i * (max_val - min_val) / (max_val - min_val) for i, min_val, max_val in zip(numbers)]

def test_rescale_to_unit(test_cases: List[List[float]]):
    # Test cases are in a nested list with three values
    assert rescale_to_unit(test_cases[0]) == [0.0, 0.0, 0.0]
    test passing the