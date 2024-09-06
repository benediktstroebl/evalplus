```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Removes all duplicate elements from a list of integers and returns a unique list. 
    """
    unique elements that appear more than once in the list
    """
    return [num for num in numbers if num not in numbers[:]]

# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [3, 2, 2, 1, 4]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 1]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5, 6]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]
```

This Python script defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a unique elements that do not appear more than once in the original list.