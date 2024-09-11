### Rolling Maximum
#### Problem: Generate a list of rolling maximum elements from a given list of integers.
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list of rolling maximum elements.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = [max(numbers[:i+1]) for i in range(len(numbers))]
    return rolling_max_list

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

### Explanation:

*   We use a list comprehension to generate the list of rolling maximum elements.
*   The `max` function returns the maximum element from the slice of the list up to the current index `i+1`.
*   The `range` function generates the indices from 0 to the length of the list minus 1.
*   The resulting list of rolling maximum elements is returned by the function.

### Time Complexity:

*   The time complexity of the `max` function is O(n) in the worst case, where n is the number of elements in the slice.
*   The list comprehension iterates over the indices of the list, so its time complexity is O(n), where n is the length of the list.
*   Therefore, the overall time complexity of the function is O(n^2) in the worst case.

### Space Complexity:

*   The list comprehension creates a new list with the rolling maximum elements, which requires O(n) space in the worst case.
*   Therefore, the space complexity of the function is O(n).