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
    # Create an OrderedDict to keep track of the count of each number
    count_dict = OrderedDict()
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Use a list comprehension to filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```

Alternatively, you can use Python's built-in `dict` to achieve the same result, but this approach does not preserve the original order:

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
    # Create a dictionary to keep track of the count of each number
    count_dict = {}
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Use a list comprehension to filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4] or [1, 4, 3] (order not guaranteed)
```

If you're using Python 3.7 or later, you can use the `dict` approach and still get the original order:

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
    # Create a dictionary to keep track of the count of each number
    count_dict = {}
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Use a list comprehension to filter out numbers that occur more than once
    result = [num for num in numbers if count_dict[num] == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # [1, 3, 4]
```