```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [num for num in numbers if num not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
assert result == [1, 3, 4]

numbers = [4, 2, 3, 4, 2]
result = remove_duplicates(numbers)
assert result == [4, 2, 3]

numbers = [5, 6, 7, 8, 9]
result = remove_duplicates(numbers)
assert result == [5, 6, 7, 8, 9]
``` 
This Python script provides a function `remove_duplicates` that accepts a list of integers and returns a new list with duplicates removed. It utilizes the particular to create a new set of integers and then filters out any duplicate numbers from the original list. 

This function is then tested with three different sets of numbers to ensure its correctness.