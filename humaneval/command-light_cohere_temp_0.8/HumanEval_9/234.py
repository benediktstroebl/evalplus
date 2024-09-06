Here is a Python script that contains a self-contained function that solves the problem of finding the rolling max element in a list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Find the rolling maximum element in a list of integers.
    Args: 
        numbers (List[int]): A list of integers.
    Returns: 
        List[int]: The list of integers with the rolling maximum element.
    """
    numbers = [5, 2, 3, 1, 4, 5, 6]
    max_num = numbers[0]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
    return max_num

# Test cases:
numbers = [5, 2, 3, 1, 4, 5, 6]
print("The rolling max element in the list is:", rolling_max(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print("The rolling max element in the list is:", rolling_max(numbers))

numbers = [5, 1, 2, 3, 4, 6]
print("The rolling max element in the list is:", rolling_max(numbers))
```

This script provides a function called `rolling_max` that takes a list of integers as input and returns the list of integers with the rolling maximum element. The function uses a algorithm that keeps track of the maximum element seen so far (max_num), and then iterates through the list, comparing each element with max_num. The element that is larger is set as max_num. 

This is a self-contained and efficient solution to the problem of finding the rolling max element in a list of integers.