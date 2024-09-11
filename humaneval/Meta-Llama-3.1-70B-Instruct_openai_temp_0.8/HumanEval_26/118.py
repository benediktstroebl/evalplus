```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an ordered dictionary to keep track of encountered elements
    encountered = OrderedDict()
    
    # Iterate over the list of numbers
    for num in numbers:
        # Add each number to the ordered dictionary
        encountered[num] = None
    
    # Filter out the elements that occur more than once
    result = [num for num in encountered if numbers.count(num) == 1]
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This script works by first creating an ordered dictionary to keep track of the elements it has encountered. This is necessary to preserve the original order of elements.

Then, it filters out the elements that occur more than once in the input list by using a list comprehension. The `numbers.count(num)` expression counts the occurrences of each number in the input list, and only includes it in the result if it occurs exactly once.

Note: The `numbers.count(num)` expression has a time complexity of O(n), where n is the length of the input list. This makes the overall time complexity of the script O(n^2), which may not be suitable for large input lists. A more efficient solution would involve using a different data structure, such as a dictionary, to count the occurrences of each number in a single pass. 

Here is an alternative version with a better time complexity:

```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dictionary to count the occurrences of each number
    counts = {}
    
    # Create an ordered dictionary to keep track of encountered elements
    encountered = OrderedDict()
    
    # Iterate over the list of numbers
    for num in numbers:
        # Increment the count of the current number
        counts[num] = counts.get(num, 0) + 1
        
        # Add each number to the ordered dictionary
        encountered[num] = None
    
    # Filter out the elements that occur more than once
    result = [num for num in encountered if counts[num] == 1]
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This version of the script has a time complexity of O(n), making it more suitable for large input lists.