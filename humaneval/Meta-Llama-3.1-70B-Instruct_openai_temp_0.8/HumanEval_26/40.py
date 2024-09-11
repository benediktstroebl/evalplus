```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers: A list of integers.
    
    Returns:
        A list of integers with duplicates removed.
    """
    seen = OrderedDict()
    for num in numbers:
        seen[num] = seen.get(num, 0) + 1
    
    return [num for num, count in seen.items() if count == 1]


# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```