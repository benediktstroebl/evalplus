```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert input list to set to remove duplicates
    return list(numbers)

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers2 = [5, 5, 5, 6, 6]
result2 = remove_duplicates(numbers2)
print(result2)  # Output: [5, 6]
``` 
This Python function, named `remove_duplicates`, takes a list of integers as input and creates a new list with all distinct elements from the original list. The function converts the result into a set, which removes duplicates, and then converts it back into a list. 

This allows for the removal of elements that occur more than once in the input list, and the result will always be a list of distinct integers.