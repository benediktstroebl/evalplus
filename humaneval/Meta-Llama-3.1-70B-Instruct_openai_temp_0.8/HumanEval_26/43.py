```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    # Create an OrderedDict to keep track of the count of each number
    count_map = OrderedDict()
    for num in numbers:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, count in count_map.items() if count == 1]

    return result


# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use a list comprehension with a dict to achieve the same result:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers.

    Returns:
        A list of integers with duplicates removed.
    """
    seen = {}
    result = []
    for num in numbers:
        if num not in seen:
            seen[num] = 1
            result.append(num)
        else:
            seen[num] += 1
            if seen[num] == 2:
                result.remove(num)
    return result
```

Both of these solutions will remove all elements that occur more than once in the input list, preserving the order of the remaining elements.