Here is a self-contained Python script that solves the problem of inserting a number 'delimiter' between every two consecutive elements of an input list:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [x, delimeter, x + delimeter] + numbers[1:]
```
This script defines a function called `intersperse` that takes a list of integers numbers and a delimiter as input and returns a new list with the inserted delimiter. The function works by creating a new list with the first and middle element of the original list, then adding the length of the delimiter and the sum of the two consecutive elements together. The process continues until the result is a list with the original input list and the inserted delimiter as elements. 

This is a self-contained function that can be used to solve the problem of inserting delimiters into lists of numbers in a straightforward and efficient manner.