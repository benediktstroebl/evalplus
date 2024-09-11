```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with no duplicates.
    """
    seen = set()
    seen_twice = set()
    result = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
        else:
            seen_twice.add(num)

    return [num for num in result if num not in seen_twice]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can solve this problem in a more Pythonic way using a list comprehension with an if condition that checks if the count of each number in the list is 1:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers (List[int]): A list of integers.

    Returns:
    List[int]: A list of integers with no duplicates.
    """
    return [num for i, num in enumerate(numbers) if numbers.count(num) == 1]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
However, the second approach is less efficient for large lists because the `count()` method has to scan the entire list for each number, resulting in a time complexity of O(n^2). The first approach has a time complexity of O(n).