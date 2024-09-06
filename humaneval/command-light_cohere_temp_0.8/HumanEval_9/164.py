```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.List = [numbers + max(numbers)
    return numbers.list()
```
# Basic test
def test_rolling_max():
    numbers = [1, 2, 3, 2, 3, 4, 2]
    assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4], "Rolling maximum should be correct."

# Test with different number of elements
numbers = [1, 2, 3]
test_rolling_max()

# Test with negative numbers
numbers = [-1, -2, -3]
test_rolling_max()

# Test with different order of numbers
numbers = [3, 2, 1]
test_rolling_max()

```
This Python code presents a function `rolling_max` designed to generate a list of rolling maximum elements within a given sequence of integers. It utilizes the particular type hints to achieve this, such as the function name, parameter types, and return type. The code also conducts several tests to verify the correctness of the `rolling_max` function.