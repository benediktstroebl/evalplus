```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling max elements in the given list.
    """
   
    list comprehension provides a simple solution, looping through the list and storing the maximum element encountered so far in a new list.
    """
    list comprehension creates a list of rolling max elements:
    [max(numbers[0], numbers[1]) , max(numbers[2], numbers[3]) , ... , max(numbers[-1], numbers[-2])]
    """
    return [x for x in numbers if x == max(numbers[i], numbers[i+1])][::-1]

# Simple test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
print("Rolling max elements:", rolling_max(numbers)) 
numbers = [5, 10, 3, 8, 2, 20, 10, 3]
print("Rolling max elements:", rolling_max(numbers)) 

```

This script defines a function named `rolling_max`, which generates a list of rolling maximum elements from a given list of integers. The function achieves this by utilizing the `max()` function along with the `list comprehension` to identify the maximum element in each rolling window. 

The `rolling_max()` function is then tested using two different sets of numbers, and the output is displayed, showing the list of rolling maximum elements.