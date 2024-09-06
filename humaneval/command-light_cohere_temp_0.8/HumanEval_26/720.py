```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all elements that occur more than once from the input list.
    Args:
        numbers (List[int]): Input list of integers.
    Returns: list of integers without duplicates.
    """
code
    ```
    input:
        numbers = [1, 2, 3, 2, 4]
    output:
        [1, 3, 4]
    """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
   return theresult
```