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
    # Create an order preserving dictionary to count occurrences of each number
    counts = OrderedDict((num, numbers.count(num)) for num in numbers)
    
    # Filter out numbers that occur more than once
    result = [num for num, count in counts.items() if count == 1]
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this solution has a time complexity of O(n^2) because of the `count` method inside the list comprehension. A more efficient solution can be achieved using a dictionary to store the counts of each number, which would have a time complexity of O(n).

Here's an optimized version of the function:

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
    # Create a dictionary to store the counts of each number
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Filter out numbers that occur more than once
    result = [num for num in numbers if counts[num] == 1]
    
    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```