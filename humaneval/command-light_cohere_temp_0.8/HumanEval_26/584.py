```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This function removes duplicate elements from a list of integers.  It uses the unique set() function to remove duplicates.