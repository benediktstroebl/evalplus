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
    # Create an ordered dictionary to preserve the order of elements
    # and automatically remove duplicates
    unique_numbers = OrderedDict()
    for num in numbers:
        unique_numbers[num] = None
    
    # Convert the ordered dictionary keys back into a list
    unique_numbers_list = list(unique_numbers.keys())
    
    # Filter out numbers that occur more than once in the original list
    result = [num for num in unique_numbers_list if numbers.count(num) == 1]
    
    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Expected output: [1, 3, 4]
```