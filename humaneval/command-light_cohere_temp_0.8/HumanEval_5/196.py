```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list."""
    result = [num for i, num in enumerate(numbers) if i != 0] + [delimeter] + [num] * (len(numbers) - 1)
    return result

# Test cases
test_data = [1, 2, 3, 4, 10, 2, 5, 6]
test_result = intersperse(test_data, 4)
print(test_result)  # Expected Output: [1, 4, 10, 2, 4, 5, 6]

test_data2 = [1, 2, 3, 4, 5, 6]
test_result2 = intersperse(test_data2, 3)
print(test_result2)  # Expected Output: [1, 3, 5, 6]
```