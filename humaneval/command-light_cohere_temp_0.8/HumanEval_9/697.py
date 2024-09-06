```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    A function to find the rolling maximum elements in a list.
    Return a maximum element in the sequence or
    any new element added 
    """
    return [num for num in numbers if num > max_occurring[num]]
 
def max_occurring(numbers: List[int]) -> List[int]:
    """ 
    Keep track of the current maximum element 
    """
    max_num = numbers[0]
    max_occurring = [max_num]
    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        max_occurring.append(max_num)
    return max_occurring
 
# Example usage 
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output should be [1, 2, 3, 3, 3, 4, 4]
max_ occurring = max_occurring(numbers)
print(max_occurring)  # Output should be [3]
``` 
The script defines a function rolling_max which takes a list of integers and returns a new list with the rolling maximum elements found until a given moment in the sequence. This function also keeps track of the maximum element found in the sequence so far. The max_occurring helper function helps to keep track of the maximum element encountered so far and return it. The example usage at the last demonstrates how the function works.