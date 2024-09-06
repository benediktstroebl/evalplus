```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Remove duplicate integers from a list.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return result
    ```

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 3, 2, 4]) == [1, 3, 4]
    assert remove_duplicates([10, 2, 3, 10, 1]) == [10, 2, 3]
    assert remove_duplicates([1, 2, 2, 3]) == [1, 2, 3]
```

This script defines a function **`remove_duplicates`** that accepts a list of integers and returns a new list with duplicate elements removed. The function utilizes a set to keep track of seen integers, then iterates through the input list, appending elements to the result list if they are not duplicates. The test function **`test_remove_duplicates`** validates the correctness of the **`remove_duplicates`** function.