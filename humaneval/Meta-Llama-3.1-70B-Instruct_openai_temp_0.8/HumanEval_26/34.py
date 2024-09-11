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
    # Create an ordered dictionary to store the count of each number
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
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

Alternatively, you can use a more concise approach using a dictionary to store the count of each number and a list comprehension to filter out duplicates:

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
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1

    return [num for num in numbers if count_dict[num] == 1]


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```