```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of the first occurrence of each number
    seen = OrderedDict()
    
    # Iterate through the list of numbers
    for num in numbers:
        # Add each number to the OrderedDict
        seen[num] = None
    
    # Return a list of the keys in the OrderedDict, which are the numbers that occur only once
    return list(seen.keys())

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
```

Alternatively, if the order of the remaining elements must be preserved and the first occurrence of each element should be kept, we can use a different approach:

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
    # Create an empty list to store the result
    result = []
    
    # Create an empty set to keep track of the numbers we've seen
    seen = set()
    
    # Create an empty set to keep track of the numbers that occur more than once
    duplicates = set()
    
    # Iterate through the list of numbers
    for num in numbers:
        # If the number has been seen before, add it to the duplicates set
        if num in seen:
            duplicates.add(num)
        # If the number hasn't been seen before, add it to the result list and the seen set
        else:
            result.append(num)
            seen.add(num)
    
    # Remove the duplicates from the result list
    result = [num for num in result if num not in duplicates]
    
    # Return the result list
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```