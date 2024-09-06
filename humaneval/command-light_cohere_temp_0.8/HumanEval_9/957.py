```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Compute and return the rolling maximum element(s) in a list of integers using sliding window 
    approach until a given moment.
    Parameters: 
    numbers (List[int]): A list of integers. 
    Returns: 
    List[int]): A list of integers where the rolling maximum will be calculated.
    """

def sliding_window_max(n: int, numbers: List[int]) -> List[int]:
    """ 
    Compute and return the maximum element(s) in a moving window of size 'n' in a list of integers.
    Parameters: 
    n (int): The size of the moving window. 
    numbers (List[int]): A list of integers.
    Returns: 
    List[int]): A list of integers with the maximum element(s) in the moving window of size 'n'.
    """
    if n == 1:
        return numbers[0]
    max_val = numbers[0]
    for num in numbers[1:]:
        if num > max_val:
            max_val = num
    return max_val

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
print(sliding_window_max(3, numbers))  # Output: 3
```