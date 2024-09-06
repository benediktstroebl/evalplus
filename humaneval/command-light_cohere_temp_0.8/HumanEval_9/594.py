Here's the solution:

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generates a list of rolling max elements in a given list.
    Args:
        numbers: list of integers
    Returns:
        list of integers with rolling max elements
    """
    rolling_max_list = [num for num in numbers if num > max_el for max_el in rolling_max_list]
    rolling_max_list.append(max(rolling_max_list))
    return rolling_max_list
```

The code defines a rolling_max function that generates a list of rolling maximum elements in a given list of integers. It iterates over the access a list of numbers and a list of their corresponding indices. Then, it iterates over the list of integers and checks if the current number is greater than the current maximum element. Finally, it appends the maximum element to the list and returns the modified list.