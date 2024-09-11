```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of unique integers from the input list, in the same order.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    # Create an empty dictionary to store the count of each number
    count_dict = {}
    
    # Iterate over the input list to count the occurrence of each number
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Create an empty list to store the result
    result = []
    
    # Iterate over the input list again to filter out numbers that occur more than once
    for num in numbers:
        if count_dict[num] == 1:
            result.append(num)
    
    # Return the result list
    return result

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

Alternatively, you can use a more pythonic approach using a list comprehension and the `dict.fromkeys()` method to remove duplicates while preserving the order:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of unique integers from the input list, in the same order.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    return list(dict.fromkeys([num for num in numbers if numbers.count(num) == 1]))

# Test the function
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

However, this approach has a time complexity of O(n^2) due to the `count()` method, which is less efficient than the first approach with a time complexity of O(n).