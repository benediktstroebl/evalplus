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
    # Create an OrderedDict to keep track of counts and preserve order
    counts = OrderedDict()
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    # Filter out numbers that occur more than once
    result = [num for num, count in counts.items() if count == 1]
    return result


# Example usage:
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```

In this code:

1.  We define a function `remove_duplicates` that takes a list of integers `numbers` as input.
2.  We create an `OrderedDict` called `counts` to store the count of each number in the input list. This preserves the order of elements.
3.  We iterate through the input list and update the counts in the `OrderedDict`.
4.  We use a list comprehension to create the result list, including only numbers that occur once (i.e., have a count of 1).
5.  We return the result list.

This approach has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.