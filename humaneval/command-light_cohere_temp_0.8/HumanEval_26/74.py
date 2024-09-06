```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from the list, and return the unique elements.
    :
    
    duplicates = set(set(numbers))
    return [x for x in numbers if x not in duplicates]

#Test the function:
numbers = [1, 2, 3, 2, 4, 3]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
This function takes a list of integers as input and returns a new list with all unique elements from the original list. The set() function is used to convert the input list into a set, which removes duplicate elements. Then, a list comprehension is used to filter the elements from the original list that are not in the set, which effectively removes duplicates and returns unique elements.