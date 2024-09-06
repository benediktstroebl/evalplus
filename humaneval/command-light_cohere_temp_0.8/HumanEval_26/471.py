```python
from typing import List
def remove_duplicates(numbers: List[int]):
    """ From a list of integers, remove all elements that occur more than once.
    Keeps only the partners in
    """
    seen: set() = set()
    result = [num for num in numbers if num not in seen]
    return result

# Test the function with a list of numbers
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```