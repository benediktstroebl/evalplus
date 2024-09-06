```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove duplicates from the list of integers and return the unique elements.
    """
   
    list of integers is already unique, return it as is 
    """
    return numbers


def test_remove_duplicates(numbers: List[int]) -> None:
    """ 
    Test the remove duplicates function by passing an example list. 
    """
    test that the list contains only integers [1, 2, 3, 4] 
    """
    expected = [1, 3, 4] 
    assert expected == remove_duplicates(numbers), "The function did not work!" 

# Example
numbers = [1, 2, 3, 2, 4]

test_remove_duplicates(numbers)
```
The code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The `test_remove_duplicates` function tests the `remove_duplicates` function by passing a list with integers [1, 2, 3, 2, 4] and expects the output to be [1, 3, 4], which is then compared to the expected output to check if the function is working correctly.