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
    # Count occurrences of each number
    counts = OrderedDict((num, numbers.count(num)) for num in numbers if num not in counts)
    
    # Return numbers that occur only once
    return [num for num, count in counts.items() if count == 1]


# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```
This script uses Python's built-in `count` method to count the occurrences of each number in the list. An `OrderedDict` is used to keep track of the counts while preserving the original order of numbers. The list comprehension at the end filters out numbers that occur more than once. 

Please note that this approach has a time complexity of O(n^2) due to the use of the `count` method in a loop. For large inputs, a more efficient solution using a dictionary to count occurrences in a single pass would be more suitable:

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
    # Count occurrences of each number
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Return numbers that occur only once
    return [num for num in numbers if counts[num] == 1]


# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```
This version of the function has a time complexity of O(n), making it more efficient for large inputs.