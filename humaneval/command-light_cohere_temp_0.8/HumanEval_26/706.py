```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from a list of integers.
    Each element is stored in a set and the duplicate ones are removed.
    return: All unique integers in the list
    """
    numbers_set = set(numbers)
    return [x for x in numbers_set if x not in numbers_set]

# Test the function
test_numbers = [1, 2, 3, 2, 4, 3, 4]
result = remove_duplicates(test_numbers)
print(result)  # Expected output: [1, 3, 4]
``` 
This Python function, `remove_duplicates`, accepts a list of integers and outputs a new list containing only the unique elements. It employs the use of a set to store the elements and then filters the set to retain only the elements that are not present in the input list.