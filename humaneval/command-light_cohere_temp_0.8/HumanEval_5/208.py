Here is a self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements in a given list:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(0, len(numbers)):
        if i % 2 == 0:  # Every other element is the delimiter
            result.append(delimiter)
        result.append(numbers[i])
    result.append(delimiter)
   return result
```

This function takes a list of numbers and a delimiter as input and returns a new list with the numbers separated by the delimiter. It uses the range-based loop and an if statement to determine when to append the delimiter and when not to append it.