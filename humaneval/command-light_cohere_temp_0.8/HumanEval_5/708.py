```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
test_data = [([1, 2, 3], [4])
test_result = intersperse(test_data[0], 4)
assert test_result == [5, 9, 7, 12]
test_result = intersperse(test_data[1], 4)
assert test_result == [9, 13, 11, 16]
```
The function `intersperse` takes a list of numbers and a delimiter as input and returns a list of the numbers with the delimiter inserted between every two consecutive elements. The test cases demonstrate the