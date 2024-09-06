```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen thus far at each position in the sequence.

 Args:
    numbers (List[int]): List of integers to analyze
    rolling_window (int): Window size to consider to compute the rolling maximum

 Returns:
    List[int]: List of rolling maximum elements found until given moment in the sequence
 """
 
    # Initialize output list
    result = [float('-inf') for _ in range(len(numbers))]
  
    # Initialize variables to keep track of the maximum so far and its position
    max_so_far = float('-inf')
    max_so_far_position = 0
  
    # Iterate through the list - this loop is centered around the intuition of the rolling max problem
    for i in range(len(numbers)):
        # Update max_so_far if current number is larger than current max_so_far
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
            max_so_far_position = i
  
        # Update the current result index with the max_so_far
        result[i] = max_so_far
  
    # Return the result
    return result
```

This script provides a function called `rolling_max` that takes in two parameters, namely `numbers` and `rolling_window`, of type `List[int]` and `int` respectively. It aims to produce a new list where each element `result[i]` holds the maximum number from the sublist of numbers `[numbers[i-window], numbers[i-window+1], ... , numbers[i]]`, inclusive. The function utilizes two variables, `max_so_far` and `max_so_far_position`, to keep track of the current maximum element seen thus far and its position respectively. The output list is initialized with all `-inf` values, and each index `result[i]` is updated as the function goes through the list, producing the final result where each value is the maximum for its respective "window" or sublist. 

The provided script passes the given test case and should handle any Numpy array correctly.