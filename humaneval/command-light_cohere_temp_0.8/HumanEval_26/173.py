```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps only thear list of unique integers.
    """
    unique(numbers)
    """
    return List(unique(numbers))

def test_remove_duplicates():
    """ Test function to verify the remove_duplicates function """
    numbers = [1, 2, 3, 2, 4, 3]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4] # Expected output: [1, 3, 4], but [1, 2, 3, 4] are duplicates.

test_remove_duplicates()
``` 
The `remove_duplicates` function takes a list of integers and removes all elements that occur more than once, and returns a new list with unique integers. The `test_remove_duplicates` function is a simple test function that creates a list of integers and passes it to the `remove_duplicates` function. 

This test ensures that the `remove_duplicates` function works correctly by removing duplicates from the input list of integers.