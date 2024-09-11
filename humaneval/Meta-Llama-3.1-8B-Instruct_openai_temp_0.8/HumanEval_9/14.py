### Rolling Maximum Elements

The following Python script defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers.

```markdown
### Code
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
    if not numbers:
        return []

    max_so_far = numbers[0]
    max_list = [max_so_far]

    for num in numbers[1:]:
        max_so_far = max(num, max_so_far)
        max_list.append(max_so_far)

    return max_list
```

### Explanation
The function `rolling_max` initializes the maximum element `max_so_far` to the first element in the list `numbers`. It also initializes an empty list `max_list` to store the rolling maximum elements. The function then iterates over the rest of the list, updating `max_so_far` to be the maximum of the current number and `max_so_far`, and appending `max_so_far` to `max_list`. Finally, the function returns `max_list`.