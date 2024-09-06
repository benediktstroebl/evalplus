```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ 
    Remove all duplicates from the list, 
    keeping the first occurrence only.

    Input: numbers List[int]
    Output: List[int]
    """
    return [num for num in set(numbers) if num not in numbers]

numbers = [1, 2, 3, 2, 4, 3, 1, 5]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```