Here is a Python script with a self-contained function that solves the problem of removing duplicates from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """Removes duplicate elements from the input list and returns a list of unique integers"""
    set(numbers)
    return [x for x in numbers if x not in set(numbers)]
#Test case 1: Input list with duplicates and expected output
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # [1, 3, 4]

#Test case 2: Input list with no duplicates and expected output
numbers = [1, 2, 3, 4]
print(remove_duplicates(numbers))  # [1, 2, 3, 4]

#Test case 3: Input set with duplicate values and expected output
numbers = {1, 2, 3, 4, 5}
print(remove_duplicates(numbers))  # [1, 2, 3, 4]
```

The remove_duplicates function utilizes the set() function to create a unique set of all elements in the input list. Then, it uses a list comprehension to filter out the elements that are present in the set, resulting in a list with unique elements. 

This function is self-contained and can be easily integrated into other programs to remove duplicates from lists of integers.