```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set(numbers)

    # Create a new list with elements that are in the set but not in the input list
    numbers_to_return = [num for num in unique_numbers if num not in numbers]

    return numbers_to_return
```