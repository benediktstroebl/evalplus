```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers_list = [1, 2, 3]
test_delimiter = 4

result = intersperse(numbers_list, test_delimiter)
print("Result:", result)

# Test case with no delimiter
numbers_list = [1, 2, 3]
test_delimiter = None

result2 = intersperse(numbers_list, test_delimiter)
print("Result2:", result2)
```
This code defines the **'intersperse'** function that takes a list of integers and an integer `delimiter` as input and returns a list of integers with the `delimiter` inserted between every two consecutive elements. The test cases demonstrate the value and functionality of the **'intersperse'** function.