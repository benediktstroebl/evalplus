```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements found in the given list.
    : The [1, 2, 3, 3, 3, 4, 4]
    """
    # Stacking and rolling the array
    max_roll = [x]
    for num in numbers:
        if num > max_roll[-1]:
            max_roll.append(num)
        else:
            max_roll[-1] = num
    # Reconstruct the list with the rolling maximum elements
    return [x for x in max_roll if x is not None]

# Test case: [1, 2, 3, 3, 4, 4]
print(rolling_max([1, 2, 3, 3, 4, 4]))
```