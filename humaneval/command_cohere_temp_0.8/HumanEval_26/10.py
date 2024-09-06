```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a self-contained function called remove_duplicates that takes a list of integers as input and returns a list of unique integers. The function utilizes the set function to remove duplicate elements from the input list, ensuring that no element value occurs more than once in the output list.