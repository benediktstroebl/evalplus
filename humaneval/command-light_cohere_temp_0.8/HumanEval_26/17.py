```python
from typing import List
def remove_duplicates(numbers: List[int]): 
    return list(set(numbers))
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only unique elements from the input. The function uses the due to the Python's `set()` function to convert the list into a set, and then back to a list to return the elements that are unique. 
This function is self-contained and can be used to solve the given problem, which is to remove duplicates from a list of integers.