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
    # Create an OrderedDict to maintain the order of elements
    # and count the occurrence of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result


# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

Alternatively, you can also use a list comprehension with a conditional statement to filter out duplicates in one line:

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
    # Create an OrderedDict to maintain the order of elements
    # and count the occurrence of each number
    count_dict = OrderedDict((num, numbers.count(num)) for num in numbers)
    
    # Filter out numbers that occur more than once
    return [num for num, count in count_dict.items() if count == 1]


# Example usage
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```