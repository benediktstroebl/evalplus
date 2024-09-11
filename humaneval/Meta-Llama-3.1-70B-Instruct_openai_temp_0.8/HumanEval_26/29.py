```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an ordered dictionary to store the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter out numbers that occur more than once
    unique_numbers = [num for num, count in count_dict.items() if count == 1]

    return unique_numbers

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

Alternatively, you can use a more concise solution with list comprehension and the `count` method:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [num for num in numbers if numbers.count(num) == 1]

# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```

However, the second solution has a time complexity of O(n^2) due to the `count` method, whereas the first solution has a time complexity of O(n) using an ordered dictionary. Therefore, the first solution is generally more efficient for large inputs.