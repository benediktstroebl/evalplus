```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with duplicates removed.
    """
    seen = set()
    result = []
    
    for num in numbers:
        # If the number has not been seen before, add it to the result and mark it as seen
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 2, 3, 4]
print(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]))  # Output: [1, 2, 3, 4]
```

In this script, we use a set called `seen` to keep track of the numbers we have seen so far. Whenever we encounter a number that is not in the `seen` set, we add it to the `result` list and mark it as seen. This way, we ensure that we only add each number to the `result` list once, even if it appears multiple times in the input list. The order of elements in the `result` list is the same as in the input list, as required.