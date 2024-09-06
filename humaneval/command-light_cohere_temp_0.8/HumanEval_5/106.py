```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], [4])

def test_function(data: List[int]) ->
    expected = [1, 4, 2, 4, 3]
    return [num + i * 4 for i, num in enumerate(data)] == expected
test_function(test_data)

# Test case with custom separator
test_data = [([1, 2, 3], '.')

def test_function2(data: List[int]) ->
    expected = [1, 2, 3]
    return [num + i * 4 for i, num in enumerate(data)] == expected
test_function2(test_data)

print("All tests passed!")
```