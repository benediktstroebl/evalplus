Here's a self-contained Python script that defines a function `rolling_max()` solving the given markdown code block problem:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list of rolling max elements from a given list of integers.
   
    Returns a maximum value of a list of integers
    """
    max_element = numbers[0]
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        elif num == current_max:
            current_max += 1
        max_element = max(max_element, current_max)
    return [max_element]

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

The provided solution includes a `rolling_max` function that takes a list of integers as input and returns a list of the rolling maximum elements. The function initializes `max_element` with the first element of the input list and then iterates through the remaining elements. It compares each element with the current maximum, updates the rolling maximum accordingly, and returns the final value.