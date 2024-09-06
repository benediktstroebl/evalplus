```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set()
    result = []

    # Loop through the input list
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)
            result.append(num)

    return result
```
Do you require any further assistance with code structure or optimization?