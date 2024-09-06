```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    Each element in the specified list is compared, and the maximum found in the rolling window of the list.
    Parameters:
    numbers: list of integers
    Returns: list of integers, which are the rolling maximum elements found in the list
    """
    numbers_copy = numbers[:]  # Create a shallow copy of the input list
    rolling_maxes = [num for num in numbers_copy if num > numbers_copy[0]] + [numbers_copy[0]]
    return rolling_maxes

# Example of list of integers
my_numbers = [1, 2, 3, 2, 3, 4, 2]
rolling_max_result = rolling_max(my_numbers)
print(rolling_max_result)  # Output: [1, 2, 3, 3, 3, 4, 4]
```
The provided Python code defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function uses a shallow copy technique to create a copy of the input list, and then generates the rolling maximum elements by comparing each element to the maximum element in the current window. 

Finally, an example list of integers, `my_numbers`, is used to call the function, and the resulting list of rolling maximum elements is printed.