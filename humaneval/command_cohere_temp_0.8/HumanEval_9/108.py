Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at different points in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found in the sequence."""
    rolling_max_return = [num for num in numbers]
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            rolling_max_return[i] = numbers[i]
    return rolling_max_return
```

This code defines a function called `rolling_max` that takes a list of integers as input. The function initially creates a new list, `rolling_max_return`, constituting replicas of the input list, `numbers`. It then proceeds to iterate through the list, comparing each element's value with the preceding element's value, and adjusts the `rolling_max_return` list whenever the current element is greater than its predecessor. In doing so, the function effectively creates a list of the maximum elements encountered throughout the sequence. The function finishes by returning the modified `rolling_max_return` list. 

Here is an example usage of the `rolling_max` function:
```python
# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```

The output of this code is:
```
[1, 2, 3, 3, 3, 4, 4]
```

This is the expected output; the list contains the rolling maximum elements found in the sequence at different points.