```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generates a list of rolling maximum elements in a given list of integers. 
    """

    list of integers is passed as an argument 
    Returns a list of integers with the maximum element rolling 
    """
    max_num = numbers[0]
    rolling_max_elements = [max_num]  # Initialize with the first element
    for num in numbers[1:]:
        current_max_num = max(max_num, num)
        rolling_max_elements.append(current_max_num)
        max_num = current_max_num 
    return rolling_max_elements
``` 
Feel sure, this Python script provides a self-contained function `rolling_max` that generates a list of rolling maximum elements in a given list of integers.  The approach is to keep the list updated with the current maximum element and reset the maximum number after each iteration.