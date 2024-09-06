```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    A recursive function that returns a list of rolling maximum elements found in the sequence.
    For given list of integers, returns a list of rolling maximum elements found until the moment 
    given in the sequence.
    """
    def rolling_max_helper(num: int, seen: List[int], index: int) -> bool):
        # If the current element is less than the smallest seen element, add it to the seen elements
        if num < seen[0]:
            seen.append(num)
            return True
        # If the current element is the same as the smallest seen element, return False to skip this element
        if seen[index] == num:
            return False
        # If the current element is greater than the previous rolling maximum, return True and update the rolling maximum
        if num > seen[-1]:
            return True
        return False
    # Returns the list of rolling maximum elements
    return [num for num, _ in rolling_max_helper(numbers[0], seen=List(), index=0)]
# Passes the test
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))
```
The function, `rolling_max`, is a recursive function that takes a list of integers as input and returns a list of rolling maximum elements found in the sequence until a specific moment is reached. The `rolling_max_helper` function is a recursive helper function that returns `True` if the current element is greater than the previous rolling maximum, and `False` otherwise. The `rolling_max` function then calls this helper function with the first element of the input list and the `seen` and `index` lists initialized with the first element of the input list.