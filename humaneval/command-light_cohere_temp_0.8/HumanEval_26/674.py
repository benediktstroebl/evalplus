```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list.
    Args:
        list(int) numbers
    Returns:
        list(unique(numbers))
    """
    set(numbers)  # Convert input list to set
    return list(set(numbers))

# Unit tests:
def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]

# Main function execution:
test_remove_duplicates()
```
This code defines a function remove_duplicates that removes duplicate elements from a given list of integers. It uses the set() to convert the input list into a set, and the set() function to extract unique elements from the set. The resulting list is then converted back to a list and returned. The function also has a unit test to ensure the correctness of the removal of duplicates. The test_remove_duplicates() function is used to run the unit tests and execute the main function.