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
        A list of integers with all duplicates removed.
    """
    # Create an ordered dictionary to store the count of each number.
    # The order of insertion is preserved in the ordered dictionary.
    count_dict = OrderedDict()
    
    # Iterate over the input list and count the occurrence of each number.
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Filter out the numbers that occur more than once.
    result = [num for num, count in count_dict.items() if count == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```

This script uses an `OrderedDict` to keep track of the count of each number in the input list while preserving the order of insertion. It then filters out the numbers that occur more than once and returns the result.

Alternatively, you can also use a simple list comprehension with a conditional statement to achieve the same result:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if numbers.count(num) == 1]
```

However, this approach is less efficient than the previous one because it uses the `count` method which has a time complexity of O(n), resulting in a time complexity of O(n^2) for the entire function. The previous approach has a time complexity of O(n).