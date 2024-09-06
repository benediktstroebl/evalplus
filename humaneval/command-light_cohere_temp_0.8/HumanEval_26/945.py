```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from the input list, returns a unique list.
    numbers = [1, 2, 3, 2, 4, 1, 3]
    result = remove_duplicates(numbers)
    assert len(result) == 3
    assert result[0] == 1
    assert result[1] == 3
    assert result[2] == 4
    assert result[3] == 2
    assert result[4] == 1
    return result
```