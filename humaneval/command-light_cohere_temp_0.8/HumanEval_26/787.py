```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input.
    """
    list comprehension with set and len as filtering mechanism.
    return [ [elements not in numbers more than once]
    """
    return [num for num in numbers if num not in numbers[numbers.count()]]
``` 
# Unit tests
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]

def test_remove_duplicates_error():
    with pytest.assert():
        assert remove_duplicates([1, 2, 3, 2]) == [1, 3, 4]
``` 
This script defines a function **`remove_duplicates`** and its corresponding tests which demonstrate its functionality and handle possible exceptions.