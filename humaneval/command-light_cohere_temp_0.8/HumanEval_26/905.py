```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the Rasistent elements in order
    """
    set_to_ removals = set(numbers)
    return [x for x in numbers if x not in set_to_removals]

def test_remove_duplicates():
    numbers = [1, 2, 3, 2, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
```