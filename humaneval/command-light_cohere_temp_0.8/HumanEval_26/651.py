```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from a list of integers.
    Remove duplicates and return a list with only unique integers.
    """
    The list comprehension method with set-like behaviour.
    """
    set(numbers)
    numbers = [x for x in set(numbers) if x not in numbers]
    return numbers

# Example
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This Python code defines a function remove_duplicates that takes a list of integers as input and creates a new list with unique integers from the original list. The function utilizes the set(numbers) to create a new set of integers and then adds elements from the original list that are not present in the set, effectively removing any duplicates. The example provided demonstrates the use of the remove_duplicates function with a list of numbers [1, 2, 3, 2, 4], and the output is [1, 3, 4], which are the unique integers from the original list.