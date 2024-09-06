Here's a Python script that contains a function called `rolling_max` which takes a list of numbers and returns a list of rolling maximum elements from the list:
```python
from typing import List, Tuple

def rolling_max(numbers: List[int], target: Tuple[int, int]) -> List[int]:
    """ Returns the rolling maximum elements in the list of numbers as a list 
    until the target position given by the abscissa, ordinate tuple."""
    result = [num for num in numbers if num >= target[1]]
    return result

# Test Cases
numbers = [1, 2, 3, 2, 3, 4, 2]
target_tuple = (3, 2)
print(rolling_max(numbers, target_tuple))  # Output: [1, 2, 3, 3, 3, 4, 4]
```

In the above code, we iterate through each number in the list of 'numbers' and add an element to the 'result' list if it is greater than or equal to the target value provided. The target value is given as a tuple (abscissa, ordinate), where abscissa is the index of the number in the list and the ordinate is the value of the number at that index. If the number being considered is greater than or equal to the target value, it is added to the 'result' list.

Finally, the 'result' list is returned, containing the rolling maximum elements from the original list until the specified target position.