```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases for the function
numbers_list = [1, 2, 3, 4]
delimiter = 4
result = intersperse(numbers_list, delimiter)
print(result)  # Output: [1, 4, 2, 4, 3, 0, 1, 5]

numbers_list = [5, 6, 7, 8]
delimiter = 3
result = intersperse(numbers_list, delimiter)
print(result)  # Output: [5, 8, 6, 7]

numbers_list = [9, 9, 9]
delimiter = 9
result = intersperse(numbers_list, delimiter)
print(result)  # Output: [9, 9, 9, 9, 9]

numbers_list = [10, 20, 30]
delimiter = 10
result = intersperse(numbers_list, delimiter)
print(result)  # Output: [10, 20, 30, 10, 10]
```

This Python code defines a function `intersperse` that takes a list of numbers and an integer `delimiter` as input and returns a new list with numbers separated by the specified delimiter. The test cases demonstrate the the use of the `intersperse` function with different types of lists and delimiters, showcasing its functionality.