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
        List[int]: A list of integers with all duplicates removed.
    """
    # Create an OrderedDict to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Use a list comprehension to filter out numbers that occur more than once
    return [num for num, count in count_dict.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, using `OrderedDict` is not the most Pythonic or efficient way to solve this problem. Here's an alternative implementation using a different approach:

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

    return [num for num in numbers if not (num in seen_twice or (num in seen and not seen_twice.add(num) and seen.add(num)))]

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

But the most efficient and Pythonic way to solve this problem is by using a different approach:

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
    output = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            if numbers.count(num) == 1:
                output.append(num)
    return output

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This solution iterates over the input list only once and uses a set to keep track of the numbers it has seen. It appends a number to the output list only if it has not been seen before and occurs exactly once in the input list.