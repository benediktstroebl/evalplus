```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set to store unique numbers
    unique_numbers = set()

    # Initialize an empty list to store the result
    result = []

    # Loop through the input list and add unique numbers to the set
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.add(num)

    # Append all elements in the set to the result list
    for num in unique_numbers:
        result.append(num)

    return result
```