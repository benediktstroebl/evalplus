```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int])` as input. Inside the function, it employs a set, which naturally eliminates duplicate elements, to process the input list. The function then returns a list containing only the unique elements from the input list, effectively removing any occurrences of duplicate integers.