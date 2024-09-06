```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = List(sorted(numbers))  # Ensure sorted order
    return [x for x in numbers if x == numbers[-1]]  # Use the last element as the rolling maximum

if __name__ == "__main__":
    numbers = [1, 2, 3, 2, 3, 4, 2]
    expected_result = [1, 2, 3, 3, 3, 4, 4]
    result = rolling_max(numbers)
    assert result == expected_result, "Error: Expected {} but got {}".format(expected_result, result)
```