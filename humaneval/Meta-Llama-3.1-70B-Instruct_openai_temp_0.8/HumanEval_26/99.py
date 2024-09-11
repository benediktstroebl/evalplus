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
    # Create an ordered dictionary to count the occurrences of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise version with a dict comprehension:

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
    # Create an ordered dictionary to count the occurrences of each number
    count_dict = OrderedDict((num, numbers.count(num)) for num in set(numbers))

    # Filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```