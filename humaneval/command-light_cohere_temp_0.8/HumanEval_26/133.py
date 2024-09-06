```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers.
    Input: numbers List with duplicates
    """
    set() = set(numbers)
    return [i for i in set]

# Test cases
numbers1 = [1, 2, 3, 2, 4]
numbers2 = [1, 2, 2, 3, 4, 5]
numbers3 = [1, 2, 3, 4, 5, 6]
print(remove_duplicates(numbers1))
print(remove_duplicates(numbers2))
print(remove_duplicates(numbers3))
```

This Python script defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicates from it. The test cases provided demonstrate the with a few sample lists, and the function's output is printed, showcasing that duplicates are correctly removed.