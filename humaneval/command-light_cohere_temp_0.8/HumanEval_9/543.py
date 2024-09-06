```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculates the rolling maximum element in a list of integers.
    Returns a max values in the list until the next update.
    """
    max_so_far = numbers[0]
    current = numbers[0]
    for num in numbers[1:]:
        current = max(num, current+num)
        max_so_far = max(max_so_far, current)
    return [max_so_far, max(max_so_far, current)]

numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

The above code defines a rolling_max function that calculates the rolling maximum element in a list of integers. The function utilizes the max_so_far and current variables to keep track of the maximum value and the current element, respectively.

The loop iterates through each element in the numbers list, updates the current and max_so_far values accordingly, and the final result is a list containing the rolling maximum value and the current element.

The output will be: `[4, 3]`