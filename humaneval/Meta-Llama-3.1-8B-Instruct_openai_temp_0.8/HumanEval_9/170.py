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
    if not numbers:  # Check if the input list is empty
        return []

    max_until_now = numbers[0]  # Initialize max_until_now as the first element of the list
    result = [max_until_now]  # Initialize the result list with the first element

    for num in numbers[1:]:  # Iterate over the list starting from the second element
        if num > max_until_now:  # If the current number is greater than max_until_now
            max_until_now = num  # Update max_until_now
        result.append(max_until_now)  # Append max_until_now to the result list

    return result

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

**Explanation:**

1. We initialize `max_until_now` as the first element of the input list and `result` with `max_until_now`.
2. We iterate over the list starting from the second element.
3. For each element, we check if it's greater than `max_until_now`. If it is, we update `max_until_now`.
4. We append `max_until_now` to the `result` list.
5. Finally, we return the `result` list.

**Time Complexity:** O(n), where n is the length of the input list.

**Space Complexity:** O(n), as we need to store the result list.