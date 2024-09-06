```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicate elements from the input list.
    """
    list(set()) == numbers
    for num in numbers:
        if num > 1:
            numbers.remove(num)
    return numbers
    return []
    return numbers

# Example
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```