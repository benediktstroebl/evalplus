```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements found until a given moment in the sequence.
    Args: 
        numbers: list of integers, the list must be non-empty and sorted.
    Returns: list of rolling maximum elements in the list.
    """
    def get_rolling_max(numbers):
        # Sort the input list
        numbers.sort()
       
        # Initialize the maximum element as first element of the list
        max_num = numbers[0]
        # Iterate over the list and update the maximum element accordingly
        for num in numbers[1:]:
            if num > max_num:
                max_num = num
        return [max_num]
    return get_rolling_max(numbers)
```

This Python script defines a function named `rolling_max`, which generates a list of the rolling maximum elements found up to a specific moment in a given list of integers. The function utilizes a test type hint for the function name and takes a single parameter called `numbers` which should be a list of integers. The function then returns a list of integers, which is a list of rolling maximum elements in the original input list.