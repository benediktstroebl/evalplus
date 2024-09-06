```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from the list.
    Input: numbers = [1, 2, 3, 2, 4]
    Output: [1, 3, 4]
    """
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
```