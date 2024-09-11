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
    # Create an OrderedDict to count occurrences of each number
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Create a new list with only the numbers that occur once
    unique_numbers = [num for num, count in counts.items() if count == 1]

    return unique_numbers

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise solution using a dictionary comprehension and a list comprehension:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {num: numbers.count(num) for num in set(numbers)}
    return [num for num in numbers if counts[num] == 1]

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this solution is less efficient than the first one because it uses the `count` method, which has to iterate over the list for each number. The first solution only iterates over the list once.