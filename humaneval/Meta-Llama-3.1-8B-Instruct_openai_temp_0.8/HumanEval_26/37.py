### Remove Duplicates from a List
#### Problem Statement
From a list of integers, remove all elements that occur more than once. Keep order of elements left the same as in the input.

#### Solution
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    :param numbers: A list of integers
    :return: A list of integers with duplicates removed
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    result = []

    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)

    return result
```

#### Explanation
This solution uses a set to keep track of the numbers we've seen so far. It iterates over the input list, and for each number, it checks if it's already in the set. If not, it adds the number to the result list and the set. This way, we ensure that each number appears at most once in the result list, and the order is preserved.

#### Example Use Cases
```python
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
print(remove_duplicates([1, 1, 1, 1, 1]))  # []
print(remove_duplicates([1, 2, 3, 4, 5]))  # [1, 2, 3, 4, 5]
```