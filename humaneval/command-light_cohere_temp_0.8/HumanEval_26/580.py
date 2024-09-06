```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate numbers from a list, returns a unique list.
    numbers = [1, 1, 2, 3, 2, 1, 4]
    result = remove_duplicates(numbers)
    assert result == [1, 3, 4]
    assert len(set(numbers)) == len(result)
    assert [x for x in numbers if x not in result] == []
    return result
```