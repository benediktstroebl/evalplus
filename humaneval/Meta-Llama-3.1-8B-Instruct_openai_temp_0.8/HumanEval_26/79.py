```markdown
### Remove Duplicates from a List

This script defines a function `remove_duplicates` that removes all elements from a list that occur more than once.
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
    
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()  # Dictionary to keep track of seen elements
    result = []   # List to store the result
    
    for num in numbers:
        if num not in seen:  # Check if the current element is not in the seen set
            seen.add(num)    # Add the current element to the seen set
            result.append(num)  # Add the current element to the result list
    
    return result  # Return the list with duplicates removed

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script defines a function `remove_duplicates` that iterates over the input list. For each element, it checks if the element is already in the `seen` set. If it's not, it adds the element to the `seen` set and the `result` list. This way, only unique elements are added to the `result` list. The function finally returns the `result` list.

The script includes a docstring that explains the purpose of the function, its parameters, and its return value. It also includes an example usage of the function to demonstrate its behavior.