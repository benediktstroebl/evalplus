```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Use an OrderedDict to keep track of the count of each number
    count_dict = OrderedDict()
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            count_dict[num] = 1

    # Create a new list that only includes numbers with a count of 1
    result = [num for num, count in count_dict.items() if count == 1]

    return result


# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```