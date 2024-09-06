```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, _ in sorted(enumer): max(numbers)]

# Sample test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
assert rolling_max(numbers) == [1, 2, 3, 3, 3, 4, 4]

numbers = [5, 10, 3, 2, 1]
assert rolling_max(numbers) == [10, 3, 2, 1]

numbers = [10, 10, 10]
assert rolling_max(numbers) == [10, 10]

numbers = [10, 10, 10, 20]
assert rolling_max(numbers) == [10, 10, 10]

numbers = [10, 20, 30, 40, 20, 10]
assert rolling_max(numbers) == [10, 20, 30, 40]
```
This Python code defines a function `rolling_max` that calculates the rolling maximum elements from a given list of integers. The function utilizes the analytical sorting and maximum taking approach to achieve this. The code then includes multiple test cases to verify the correctness of the `rolling_max` function, which demonstrates its intended behavior for various input scenarios.