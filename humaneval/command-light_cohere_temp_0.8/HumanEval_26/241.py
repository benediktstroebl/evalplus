```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
The function takes a list of integers as input and returns a new list with unique integers. The set() function is used to remove the duplicates, and the list() function is used to convert the set back into a list.