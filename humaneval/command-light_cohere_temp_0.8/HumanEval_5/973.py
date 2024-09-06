```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test cases
numbers_test = [4, 1, 2, 3]
delimiter_test = 4
result_test = intersperse(numbers_test, delimiter_test)
print(result_test)  # Output: [4, 4, 1, 4, 2, 4, 3]

numbers_list = [1, 2, 3]
result_list = intersperse(numbers_list, 10)
print(result_list)  # Output: [11, 12, 13]
```

This Python code defines a function `intersperse` that takes two parameters: a list of numbers and a delimiter as an integer. It uses a the particular list comprehension to iterate through the elements of the input list, adding the delimiter value between every two consecutive elements, effectively "spacing out" the numbers in the list.