```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    - Handle empty input list gracefully
    - Test with various inputs to ensure correct behavior
    """
    if not numbers:
        return []

    # Insert delimiter between every two consecutive elements
    result = [num] + [delimeter] + [num + delimeter] + [num + 2 * delimeter] + [num + 3 * delimeter]
    for num in numbers[1:]:
        result += [delimeter] + [num + delimeter] + [num + 2 * delimeter] + [num + 3 * delimeter]
    return result[:]
```