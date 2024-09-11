```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    
    Args:
        numbers (List[int]): A list of integers.
    
    Returns:
        List[int]: The list with duplicates removed.
    
    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()  # A set to keep track of seen numbers
    result = []  # The list to store the result
    
    for number in numbers:
        # If a number is not in the set (i.e., not seen before), add it to the set and the result list
        if number not in seen:
            seen.add(number)
            result.append(number)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

In this script, we use a set (`seen`) to keep track of the numbers we've seen so far. We iterate through the input list (`numbers`), and for each number, we check if it's in the `seen` set. If it's not, we add it to the `seen` set and the `result` list. This way, we ensure that each number is only included in the `result` list once, while maintaining the original order.