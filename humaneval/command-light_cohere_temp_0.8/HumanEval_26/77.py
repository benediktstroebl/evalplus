Here is a self-contained Python script that solves the problem you described:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
```

This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with all distinct integers. The function uses a set to keep track of numbers that have been seen before and then filters out any duplicates from the input list. This results in a unique list of integers, which are then returned by the function.

Here are some sample test cases for the remove_duplicates function:
```python
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 3, 4]

numbers = [1, 2, 3, 4, 5]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 1]
result = remove_duplicates(numbers)
print(result)
# expected output: [1, 2, 3, 4]
```