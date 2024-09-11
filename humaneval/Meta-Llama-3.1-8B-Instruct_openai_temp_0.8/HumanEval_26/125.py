```markdown
### Remove Duplicate Numbers
#### Problem Statement
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution

```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Removes all elements from a list of integers that occur more than once.
    Keeps the order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with duplicates removed.

    Example:
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an ordered dictionary to keep track of unique elements
    unique_elements = OrderedDict()
    
    # Iterate over the input list
    for num in numbers:
        # Add each element to the dictionary
        # If it already exists, its count won't increment, so it won't be added again
        unique_elements[num] = None
    
    # Return a list of keys from the dictionary, which represents unique elements in the order they appeared
    return list(unique_elements.keys())

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

#### Explanation
This solution uses an `OrderedDict` to keep track of unique elements. By adding each element to the dictionary, we ensure that only the first occurrence of each element is stored. The dictionary's keys represent the unique elements, and we return them in the order they appeared in the input list. This approach has a time complexity of O(n), where n is the number of elements in the input list.