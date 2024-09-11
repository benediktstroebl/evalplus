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
    # Create an ordered dictionary to keep track of the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out the numbers that occur more than once
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

Alternatively, you can also solve this problem using a list comprehension with a conditional statement that checks the count of each number in the list, like so:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
    numbers: A list of integers.

    Returns:
    A list of integers with duplicates removed.
    """
    return [num for i, num in enumerate(numbers) if numbers.count(num) == 1 and numbers.index(num) == i]


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

However, please note that this approach is less efficient for large lists because it uses the `count` and `index` methods inside a loop, resulting in a time complexity of O(n^2). The first approach using an ordered dictionary has a time complexity of O(n).