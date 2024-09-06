```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1: Simple list with single delimiter
numbers = [1, 2, 3]
delimiter = 4
result = intersperse(numbers, delimiter)
print(result)

# Test case 2: Empty list
numbers = []
result = intersperse(numbers, 10)
print(result)

# Test case 3: List with single element
numbers = [10]
result = intersperse(numbers, 3)
print(result)

# Test case 4: List with multiple elements and custom delimiter
numbers = [1, 2, 3]
delimiter = 'abc'
result = intersperse(numbers, delimiter)
print(result)
```
This code defines a `intersperse` function that takes a list of integers and a delimiter as input, and returns a new list with the integers separated by the given delimiter. The test cases demonstrate the specifically how the function works with various scenarios: This enhances the clarity and readability of the code, while also making it more efficient and easier to understand.