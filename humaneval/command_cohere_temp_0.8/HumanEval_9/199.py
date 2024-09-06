```python
from typing import List, Tuple

def rolling_max(numbers: List[int], rolling_window: int) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum elements seen until the current moment
    in the sequence.
    
    Args:
        numbers (List[int]): The list of integers to be processed.
        rolling_window (int): The size of the rolling window to look at to find the rolling maximum.
    
    Returns:
        List[int]: A list of integers, where each integer represents the maximum of rolling_window size interval found
                    in the original sequence.
    """
    
    if not numbers or not rolling_window:
        return []

    # Sort the input list to find the maximum elements easily.
    sorted_numbers = sorted(numbers)
    
    # Calculate the rolling maximum elements for each index in the rolling window.
    rolling_max_elements = [sorted_numbers[i] for i in range(len(sorted_numbers)-rolling_window+1)]
    
    return rolling_max_elements
```

The code has a `rolling_max` function that takes in two parameters: `numbers` which is the list of integers to process, and `rolling_window` which is the size of the moving window. The function proceeds to sort the `numbers` list and then iterates over the range of indices that correspond to rolling windows. The values at these indices are used as the rolling maximum for the corresponding window. The result is returned as a list of these rolling maximums. 

The script can be tested by calling the function with a sample input and verifying that the output matches the expected result. 

For example:
```python
test_numbers = [1, 2, 3, 2, 3, 4, 2]
test_rolling_window = 3

expected_result = [1, 2, 3, 3, 3, 4, 4]

assert rolling_max(test_numbers, test_rolling_window) == expected_result
``` 
The function can also be tested using the `>>>` operator, as described in the docstring example.