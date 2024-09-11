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
    # Create an OrderedDict to keep track of element counts while preserving order
    count_dict = OrderedDict()
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in count_dict:
            count_dict[num] += 1
        # Otherwise, add it to the dictionary with a count of 1
        else:
            count_dict[num] = 1

    # Use a list comprehension to filter out numbers with counts greater than 1
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
In this script, we use an `OrderedDict` to keep track of the count of each number in the input list. We then use a list comprehension to create a new list that includes only the numbers with a count of 1, effectively removing duplicates while preserving order.