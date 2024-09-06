```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    unique_numbers = set()
    result = []

    # Loop through the input list
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            result.append(num)

    return result
```

This function, `remove_duplicates`, takes a list of integers as input and returns a new list with all integers unique within the input list. It uses a unique set data structure to keep track of unique integers and removes duplicate numbers from the input list.