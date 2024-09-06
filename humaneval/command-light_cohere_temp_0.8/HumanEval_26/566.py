```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all elements that occur more than once from a list of integers.
    """
    unique = set(numbers)
    return [num for num in numbers if num not in unique]
``` 
This function utilizes the 'set' function to create a unique set of the input 'numbers'. The function then iterates through the original list, checking if each number is not already present in the set. This ensures that duplicate numbers are effectively removed, and the function returns a new list with the remaining unique integers.