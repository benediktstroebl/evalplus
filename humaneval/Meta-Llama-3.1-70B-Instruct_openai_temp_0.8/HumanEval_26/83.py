```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count_dict = OrderedDict()
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    return [num for num, count in count_dict.items() if count == 1]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, the above code may not be the most efficient way to solve this problem, especially for larger lists, because it needs to iterate over the list twice (once to count the occurrences, once to create the output list).

A more efficient solution would be to use a single pass through the list and keep track of the count of each number and whether it has been added to the output list. Here's an example of how to do it:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count_dict = {}
    result = []
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
            result.append(num)
        else:
            if count_dict[num] == 1:
                result.remove(num)
            count_dict[num] += 1

    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, this solution still involves removing elements from the result list, which can be inefficient if the list is large.

Here is a revised solution that avoids this problem:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    count_dict = {}
    for num in numbers:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    return [num for i, num in enumerate(numbers) if count_dict[num] == 1 and numbers.index(num) == i]


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

However, using `numbers.index(num)` is also inefficient because it searches the list from the beginning for each number.

A more efficient solution would be to keep track of the first occurrence of each number:

```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
   