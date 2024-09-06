```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test case 1
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
print(intersperse(numbers, delimiter))  # expected output: [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3, 4, 5]
delimiter = 6
expected = [1, 8, 12, 16, 20]
print(intersperse(numbers, delimiter))  # expected output: [1, 8, 12, 16, 20]

# Test case 3
numbers = [1, 2, 3, 4, 5, 6]
delimiter = 7
expected = [2, 10, 13, 19]
print(intersperse(numbers, delimiter))  # expected output: [2, 10, 13, 19]
```

This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input, and returns a new list with numbers separated by the given delimiter. The code then provides three test cases to verify the correctness of the `intersperse` function, passing in different lists of numbers and delimiters. The output of each function is expected to be the resulting list with proper separation of numbers.