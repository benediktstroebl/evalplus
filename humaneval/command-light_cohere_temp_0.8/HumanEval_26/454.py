Here's a self-contained Python script that defines a function remove_duplicates with tests:
```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """
    From a list of integers, remove all elements that occur more than once.
    Returns: list of unique elements.
    """
example
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    numbers = set(numbers)  # Convert to set to remove duplicates
    return list(numbers)

# Test cases
test_remove_duplicates_empty = List()
test_remove_duplicates_single = List([1])
test_remove_duplicates_multiple = List([1, 2, 3, 4])

def test_remove_duplicates(*args):
    assert remove_duplicates(*args) == args[0]

test_remove_duplicates_empty.set()
test_remove_duplicates_single.set([1])
test_remove_duplicates_multiple.set([1, 2, 3, 4])

# Main function to call tests
if __name__ == "__main__":
    import pytest
    pytest.check()()