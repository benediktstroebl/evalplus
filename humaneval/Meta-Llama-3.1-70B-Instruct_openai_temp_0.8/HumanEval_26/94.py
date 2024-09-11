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
    # Create an OrderedDict to count the occurrences of each number
    # and maintain the insertion order
    count_map = OrderedDict()
    for num in numbers:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
    
    # Filter out numbers that occur more than once
    result = [num for num, count in count_map.items() if count == 1]
    
    return result


# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise solution using `dict` from Python 3.7+ which maintains the insertion order by default:

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
    count_map = {}
    for num in numbers:
        count_map[num] = count_map.get(num, 0) + 1
    
    return [num for num, count in count_map.items() if count == 1]


# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```