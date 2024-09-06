```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list and returns the unique elements in order.
    """
    for num in numbers:
        if num > 0 and num not in numbers:
            numbers.append(num)
    return numbers
```
The function remove_duplicates takes a list of integers as input and returns a new list with all duplicate elements removed. The function uses a for each number in the input list, and if the number is greater than 0 and not in the list, it is appended to the list.