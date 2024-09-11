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
    """
    if not numbers:
        return []
    
    max_so_far = numbers[0]
    result = [max_so_far]

    for num in numbers[1:]:
        if num >= max_so_far:
            max_so_far = num
            result.append(max_so_far)
        else:
            result.append(max_so_far)

    return result

# Example usage:
print(rolling_max([1, 2, 3, 2, 3, 4, 2]))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In this code, we initialize the `max_so_far` variable with the first element of the `numbers` list and the `result` list with this same element. Then, we iterate over the rest of the list. If we encounter an element that is greater than or equal to the current `max_so_far`, we update `max_so_far` and append it to the `result`. If the element is less than `max_so_far`, we simply append `max_so_far` to the `result`. This way, we keep track of the maximum element seen so far in the sequence.