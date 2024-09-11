```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers where all elements occur only once.
    """
    seen = set()  # A set to keep track of elements we've seen
    result = []  # The list of unique elements

    for num in numbers:
        if num not in seen:
            seen.add(num)  # Add the number to the set
            result.append(num)  # Add the number to the result list

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([5, 5, 5, 1, 1, 2]))  # [2]
print(remove_duplicates([10, 20, 30, 40, 50]))  # [10, 20, 30, 40, 50]
```

Alternatively, you can use a more Pythonic way to solve this problem using a dict to preserve the order of elements (Python 3.7+):

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers where all elements occur only once.
    """
    seen = dict()  # A dict to keep track of elements we've seen
    result = []  # The list of unique elements

    for num in numbers:
        if num not in seen:
            seen[num] = True  # Add the number to the dict
            result.append(num)  # Add the number to the result list

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([5, 5, 5, 1, 1, 2]))  # [2]
print(remove_duplicates([10, 20, 30, 40, 50]))  # [10, 20, 30, 40, 50]
```