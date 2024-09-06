```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return thelist of result
``` 
This code implements a function called remove_duplicates that takes a list of integers and returns a new list that contains unique integer values from the input list. It uses a unique set data structure to track the uniqueness of each integer, and it iterates through the input list, adding each integer to the set if it is not already present. The function then constructs a list of all unique integers and returns it as the result. 

This is a self-contained solution to the provided problem.