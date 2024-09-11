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

    # Create an empty dictionary to store the count of each number
    count_dict = {}

    # Iterate over the list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Use a list comprehension to create a new list with numbers that occur only once
    result = [num for num in numbers if count_dict[num] == 1]

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

This script works by first counting the occurrence of each number in the input list, and then creating a new list that includes only the numbers that occur once. The order of elements in the output list is the same as in the input list, as required by the problem statement.

Alternatively, you can also use a more concise version using a `OrderedDict` to maintain the order of elements:

```python
from collections import OrderedDict
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

    # Create an ordered dictionary to store the count of each number
    count_dict = OrderedDict()

    # Iterate over the list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Use a list comprehension to create a new list with numbers that occur only once
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Or even more concise version using `dict` with Python 3.7+:

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

    # Use dict to count the occurrence of each number and maintain the order
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    # Use a list comprehension to create a new list with numbers that occur only once
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```