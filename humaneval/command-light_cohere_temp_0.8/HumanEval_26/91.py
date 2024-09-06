Here is a self-contained Python function that removes duplicates from a list of integers:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert list to set to remove duplicates
    return list(numbers)
```

This function takes a list of integers as input and returns a new list with duplicate values removed. The function uses the set data structure to automatically remove any values that appear more than once, and then converts the set back into a list to be returned. 

This function is self-contained, meaning it can be used to solve the problem and pass all the corresponding tests without depending on external variables.