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
    # Create an OrderedDict to count the occurrence of each number
    # and preserve the order of the first occurrence.
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    
    # Filter out the numbers that occur more than once.
    return [num for num, count in counts.items() if count == 1]


# Example usage:
if __name__ == "__main__":
    print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]
```
This script defines a function `remove_duplicates` that takes a list of integers, removes duplicates while preserving the original order, and returns the resulting list. The function uses an `OrderedDict` to count the occurrence of each number and then filters out the numbers that occur more than once. The example usage demonstrates how to use the function with the provided test case.