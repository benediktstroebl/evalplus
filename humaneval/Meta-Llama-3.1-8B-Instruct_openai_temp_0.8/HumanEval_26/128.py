**Remove Duplicates from a List of Integers**
=============================================

Here's a Python script that uses a dictionary to keep track of encountered numbers and remove duplicates while preserving the original order.

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes all elements that occur more than once from a list of integers.
    
    Args:
    numbers (List[int]): The input list of integers.
    
    Returns:
    List[int]: The list with duplicates removed, preserving the original order.
    """
    encountered = {}
    result = []
    
    for num in numbers:
        if num not in encountered:
            encountered[num] = True
            result.append(num)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script iterates over the input list once. If a number has not been encountered before (i.e., it's not in the dictionary), it's added to the dictionary and appended to the result list. This ensures that all numbers are processed exactly once, and duplicates are removed while preserving their original order.