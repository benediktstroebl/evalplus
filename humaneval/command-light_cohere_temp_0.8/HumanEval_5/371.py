```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num + delimeter for num in numbers] + [num for num in numbers]
    return result

# Test cases
test_data = [([1, 2, 3], [4, 5])

def test_function(data: List[int]) -> List[int]:
    expected = [1, 4, 2, 4, 5]
    return test_data(expected)

test_cases = [test_function, [1, 2, 3], [4, 5])

# Print the test results
print("Test cases:", test_cases)
print("Expected:", [list(map(int, expected))])

# Result should be the same as expected
```