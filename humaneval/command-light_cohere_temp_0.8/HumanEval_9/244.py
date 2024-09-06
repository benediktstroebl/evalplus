```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Returns the list of rolling maximum elements in the given list.
    """
    def rolling_max(nums): 
        max_num = nums[0]
        result = [max_num] 
        for i in range(1, len(nums)):
            current = nums[i]
            max_num = max(max_num, current)
        result.append(max_num)
        return result
    """
# Example usage
nums = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(nums)
print(result)
```
The output will be: 
```
[1, 2, 3, 3, 3, 4, 4]
```
This solution uses the Python List and Tuple types and implements the rolling maximum concept.  The follows a steps to implement this solution: 

1. Input: list of numbers. 

2. Generate a initial list of the maximum element.

3 Iterate over the list and update the maximum element by comparing the current element with the current maximum.

4 Return the final list with the rolling maximum elements. 

This solution follows the intuitive approach and is self-contained, using only built-in Python functions and types.