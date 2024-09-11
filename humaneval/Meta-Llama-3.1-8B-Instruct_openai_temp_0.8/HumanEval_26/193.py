```markdown
### Removing Duplicates from a List of Integers

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all elements that occur more than once removed. The order of elements in the new list is the same as in the input list.

#### Code

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): The input list of integers.

    Returns:
        List[int]: A new list with duplicates removed.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Create an empty dictionary to store the count of each number
    count_dict = {}
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in numbers:
        # If the number is not in the dictionary, add it with a count of 1
        if num not in count_dict:
            count_dict[num] = 1
        # If the number is already in the dictionary, increment its count
        else:
            count_dict[num] += 1
    
    # Iterate over the input list again
    for num in numbers:
        # If the count of the number is 1, add it to the result list
        if count_dict[num] == 1:
            result.append(num)
    
    # Return the result list
    return result

# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
```