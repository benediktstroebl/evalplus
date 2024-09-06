Here's a self-contained Python function that solves the markdown code block problem:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+j for i,j in zip(numbers,numbers[1:]+[delimeter]])


# Test cases
numbers = [1, 2, 3]
print(inpersepe(numbers, 4))  # expected output: [1, 4, 2, 4, 3]

numbers = [10, 20, 30]
print(inpersepe(numbers, 4))  # expected output: [10, 14, 18, 22, 30]

numbers = [10, 20, 30, 40]
print(inpersepe(numbers, 4))  # expected output: [10, 14, 18, 22, 36]

numbers = [1, 2, 3, 4, 5]
print(inpersepe(numbers, 3))  # expected output: [1, 3, 4, 5]
```
This script defines a function `inpersepe` that takes a list of numbers and a delimiter as input, and returns a new list where every element is incremented by the corresponding element from the original list and the delimiter. It also provides several test cases to verify the functionality of the function.

Let me add some additional markdown code blocks with code to make the output more readable and interesting!