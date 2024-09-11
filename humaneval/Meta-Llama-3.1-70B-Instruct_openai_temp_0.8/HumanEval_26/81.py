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
    # Create an OrderedDict to store the count of each number
    count = OrderedDict()
    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, freq in count.items() if freq == 1]

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, the above solution has a time complexity of O(n) but uses extra space for OrderedDict.

Alternatively, you could use a one-liner Python solution with list comprehension, but this approach has a higher time complexity due to the `count` function.

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
    return [num for i, num in enumerate(numbers) if numbers.count(num) == 1 and numbers.index(num) == i]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
But consider this alternative solution that utilizes the `collections.Counter` class with a time complexity of O(n):

```python
from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    count = Counter(numbers)
    return [num for num in numbers if count[num] == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```