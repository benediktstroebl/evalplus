```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers

    Returns:
        A list of integers with duplicates removed
    """
    # Count occurrences of each number
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Filter out numbers with more than one occurrence
    result = [num for num, count in counts.items() if count == 1]

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, I would suggest using a more idiomatic Python solution, which uses a dictionary comprehension to count occurrences of each number and then a list comprehension to filter out numbers with more than one occurrence. Here's how you could implement this:

```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers: A list of integers

    Returns:
        A list of integers with duplicates removed
    """
    # Count occurrences of each number
    counts = {num: numbers.count(num) for num in set(numbers)}

    # Filter out numbers with more than one occurrence
    return [num for num in numbers if counts[num] == 1 and (counts[num] := counts[num] - 1) >= 0]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```