```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicate elements from the input list.
    """
    unique elements from the using set(), and then back to the original list.
    """
    return list(set(numbers))
    """
    # Implement your algorithm here
    # For demonstration, using set() to remove duplicates
    return set(numbers)

# Test the function
numbers_list = [1, 2, 3, 2, 4, 2, 3, 5]
result = remove_duplicates(numbers_list)
print(result)

numbers_set = {1, 2, 3, 4, 5}
result = remove_duplicates(numbers_set)
print(result)

```
This Python script defines a function remove_duplicates that removes duplicate elements from a list of integers. The function utilizes the unique elements using set(), and then back to the original list. 

The function is tested with two examples: a list of integers and a set of integers. 
The output is then displayed.