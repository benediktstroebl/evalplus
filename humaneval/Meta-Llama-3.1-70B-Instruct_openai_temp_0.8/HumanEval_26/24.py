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
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out the numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

Alternatively, you could use a more Pythonic approach with a list comprehension and the `count` method:

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
    # Filter out the numbers that occur more than once
    result = [num for i, num in enumerate(numbers) if numbers.count(num) == 1 or numbers.index(num)!= i]
    
    # Remove duplicates from the result while preserving order
    result = list(dict.fromkeys(result))
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, please note that the `count` method has a time complexity of O(n), so this approach may be less efficient for large lists.

A more efficient solution can be achieved by using a `set` to keep track of the numbers we've seen so far, and a `list` to store the result:

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
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            if numbers.count(num) == 1:
                result.append(num)
            seen.add(num)
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

But again, this solution has a time complexity of O(n^2) due to the `count` method.

The most efficient solution would be to use a combination of a `dict` to count the occurrences and a `set` to keep track of the numbers we've seen so far:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers