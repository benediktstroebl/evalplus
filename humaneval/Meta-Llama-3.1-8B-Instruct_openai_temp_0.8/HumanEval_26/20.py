```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of integers with no duplicates, in the same order as the input.

    Example:
        >>> remove_duplicates([1, 2, 3, 2, 4])
        [1, 3, 4]
    """
    seen = set()
    result = []
    
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    
    return result

# Example usage:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```

This Python script does the following:

1.  It defines a function `remove_duplicates` that takes a list of integers `numbers` as input.
2.  It uses a set `seen` to keep track of the numbers it has seen so far. A set in Python is an unordered collection of unique elements, which makes it ideal for tracking unique elements.
3.  It initializes an empty list `result` to store the numbers that are not duplicated.
4.  It iterates over the input list `numbers`. For each number `num`, it checks if `num` is not in the set `seen`. If `num` is not in `seen`, it means that `num` is not a duplicate and has not been seen before, so it appends `num` to the `result` list and adds `num` to the `seen` set.
5.  Finally, it returns the `result` list, which contains the numbers from the input list with no duplicates and in the same order as the input.

The time complexity of this solution is O(n), where n is the length of the input list, because it makes a single pass through the input list. The space complexity is also O(n) because in the worst case, the `seen` set and the `result` list can both grow up to the size of the input list.