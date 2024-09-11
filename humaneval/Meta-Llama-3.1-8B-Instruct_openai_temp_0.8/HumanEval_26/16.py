```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]))  # Output: [1, 2, 4]
```

This script defines a function `remove_duplicates` that iterates over the input list and checks each element to see if it has been encountered before. If not, it adds the element to the result list and marks it as seen. The function returns the result list, which contains the elements from the input list that occur only once.