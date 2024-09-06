```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Unit tests
numbers_list = [1, 2, 3]
delimiters_list = [0, 4]
result = intersperse(numbers_list, delimiters_list)

print("Test 1:", result)

numbers_list = [10, 20, 30]
delimiters_list = [5, 10]
result = intersperse(numbers_list, delimiters_list)

print("Test 2:", result)

numbers_list = [10, , 30]
delimiters_list = [5, 10]
result = intersperse(numbers_list, delimiters_list)

print("Test 3:", result)
```