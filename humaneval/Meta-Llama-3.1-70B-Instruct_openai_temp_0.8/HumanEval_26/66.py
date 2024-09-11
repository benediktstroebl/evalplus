```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with all duplicates removed.
    """
    seen = set()
    seen_twice = set()
    result = []

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
        elif num not in seen_twice:
            result.remove(num)
            seen_twice.add(num)

    return [x for x in numbers if x in seen and x not in seen_twice]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 3, 5]
```
Alternatively, you can also use a single dictionary to count the occurrences of each number:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    return [num for num in numbers if counts[num] == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 3, 5]
```