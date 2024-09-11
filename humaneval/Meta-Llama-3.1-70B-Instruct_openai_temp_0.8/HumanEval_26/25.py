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
        if num in seen_twice:
            continue
        if num in seen:
            seen_twice.add(num)
            result = [x for x in result if x!= num]
        else:
            seen.add(num)
            result.append(num)

    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 4, 5, 5]))  # [3, 4]
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
```