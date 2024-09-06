```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set to store unique values
    unique_values = set()
    
    # Initialize an empty list to store the results
    results = []
    
    for num in numbers:
        if num not in unique_values:
            unique_values.add(num)
            results.append(num)
    
    return results
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers. The function uses the use of a `set` to remove duplicate values and a list comprehension to filter out the unique values and append them to a new list.