```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])] + numbers[:-1]

# Test cases
numbers = [1, 2, 3]
print(inspersing(numbers, 4))  # expected output: [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
print(inspersing(numbers, 4))  # expected output: [10, 14, 18, 20, 30]

numbers = [10, 20, 30, 40]
print(inspersing(numbers, 4))  # expected output: [10, 14, 18, 22, 30]

numbers = [1, 2, 3, 4, 5]
print(inspersing(numbers, 5))  # expected output: [1, 6, 8, 11]

numbers = ['a', 'b', 'c', 'd']
print(inspersing(numbers, 3))  # expected output: ['a', 'b', 'c', '']
```

The provided Python code defines a function called `inspersing` that separates elements of a list using a specified delimiter and then restarts the resulting list with the original elements and the delimiter. This function is by iterating through pairs of elements and appending them with the delimiter, then combining the elements of the original list and the appended delimiter.