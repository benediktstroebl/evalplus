```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [x for x in numbers if x not in numbers[numbers.get(x)]
```
This function iterates through the input list of integers and returns a new list with all unique (i. It uses the unique method along a list comprehension to remove all duplicates from the list.