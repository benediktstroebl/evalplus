```python
from typing import List
from collections import OrderedDict

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dictionary where keys are the numbers and values are their counts
    counts = OrderedDict()
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1

    # Filter out numbers that occur more than once
    unique_numbers = [num for num, count in counts.items() if count == 1]

    return unique_numbers

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]
```
This solution works by first counting the occurrences of each number in the input list using an `OrderedDict`, which preserves the original order of elements. Then it filters out the numbers that occur more than once and returns the result.