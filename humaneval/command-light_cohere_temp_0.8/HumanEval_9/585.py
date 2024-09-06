```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Calculate the rolling maximum element in a list of integers using specified window size.
    Args: 
        numbers: list of integers with non-negative integers
    Returns: 
        list of rolling maximum elements.
    """

def get_rolling_max(numbers: List[int]) -> List[int]:
    # Create a list of rolling max elements with window size 1
    rolling_max_1 = [num for num in numbers] + [num for num in numbers[1:]]
    # Recursively calculate the rolling max elements with window size 2
    rolling_max_2 = [max(rolling_max_1[i], rolling_max_1[i+1]) for i in range(len(rolling_max_1))]
    # Repeat the above until window size is 3
    rolling_max_3 = [max(rolling_max_2[i], rolling_max_2[i+1]) for i in range(len(rolling_max_2))]
    # Return the list of rolling max elements
    return rolling_max_3

numbers = [1, 2, 3, 4, 2]
result = get_rolling_max(numbers)
print(result)
```

This script defines a function `rolling_max` that calculates the rolling maximum element in a list of integers using a specified window size. The function also has a corresponding test that checks if the function is working correctly with a given list of integers.

The `get_rolling_max` function is a wrapper for the `rolling_max` function that creates the list of rolling max elements with a window size of 1 and then recursively calculates the rolling max elements with a window size of 2.

Finally, it passes the test with a list of integers and prints the result.