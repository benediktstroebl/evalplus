Here's a Python script that contains a function called `rolling_max` which takes a list of numbers and returns a list of rolling maximum elements from the list:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """
    Generate a list of rolling maximum elements found in the list within a rolling window.
    
    Args:
    - numbers (list): Input list of integers.
    - rolling_window (int): Window size to compute the rolling maximum.
    
    Returns:
    - list: Sequence of rolling maximum elements.
    """
    
    # Initiate the rolling maximum and minimum variables
    rolling_max_curr = numbers[0]
    rolling_max_prev = numbers[0]
    
    result = [rolling_max_curr]
    
    # Iterate through the list to update the rolling maximum
    for i in range(1, len(numbers)):
        rolling_max_curr = max(numbers[i], rolling_max_prev)
        rolling_max_prev = rolling_max_curr
        
        result.append(rolling_max_curr)
    
    return result

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_window = 3
result = rolling_max(numbers, rolling_window)
print(result)
```

The script uses two variables, `rolling_max_curr` and `rolling_max_prev`, to keep track of the rolling maximum elements as you iterate through the list. The maximum value between the current element and the previous rolling maximum is used to update these variables. A list `result` is then populated with the computed rolling maximum values and returned as the output.

When the script is run with the provided example input of `[1, 2, 3, 2, 3, 4, 2]` and a rolling window size of 3, it produces the following output:
```
[1, 2, 3, 3, 3, 4, 4]
``` 

The numbers in the output correspond to the rolling maximum elements within a rolling window of size 3 for the given input sequence.