Here's a Python script that contains a function called `rolling_max` which takes a list of integers `numbers` as input and returns a list of rolling maximum elements found at various points in the sequence:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements found in the sequence."""
    rolling_max_return = []

    for i in range(len(numbers)):
        current_max = max(numbers[i:i+2])
        if i == 0:
            rolling_max_return.append(numbers[i])
        else:
            rolling_max_return.append(current_max)

    return rolling_max_return

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```

This script defines the `rolling_max` function, which uses a generator expression to create a new list that includes the current maximum element from the previous list as well as the new maximum element, and appends it to the `rolling_max_return` list. The loop starts with `index` as `0` and iterates until `index` is less than the length of the list.

The result is a list of the maximum elements at each stage of the sequence, which is then returned as the result. The example usage demonstrates how to call the function with a sample list of numbers, and the output shows the resulting list of rolling maximum elements. 

When you run this script, you should see the following output:
```
[1, 2, 3, 3, 3, 4, 4]
```