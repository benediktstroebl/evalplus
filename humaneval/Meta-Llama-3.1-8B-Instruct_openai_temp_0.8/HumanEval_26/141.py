```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): The list of integers to remove duplicates from.
    
    Returns:
        List[int]: The list with all elements that occur more than once removed.
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

However, Python has a built-in `dict` that can also be used to remove duplicates from a list while preserving the order. Here's how you can use it:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): The list of integers to remove duplicates from.
    
    Returns:
        List[int]: The list with all elements that occur more than once removed.
    """
    seen = {}
    result = []
    
    for num in numbers:
        if num not in seen:
            seen[num] = True
            result.append(num)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```

This version is a bit more memory efficient because it doesn't create a set and instead uses a dictionary to keep track of the elements it has seen so far.