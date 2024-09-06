```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements from the input list.

    Retrieves the kind of list of maximum elements from the input list, 
    where the order matters and is calculated using a sliding window.

    Example: - List comprehension: Returns a list of all elements 
    which are larger than the current maximum element after 
    applying the rolling update rule.

    Input: A list of integers (numbers)
    Output: A list of integers (rolling_max) 
    """
    numbers.append(max(numbers))
    rolling_max = [x for x in numbers if x > max(numbers)]
    return rolling_max

# Test cases
test_rolling_max = [5, 6, 7, 1, 9, 10, 8]
print(rolling_max(test_rolling_max))  # [9, 10, 10, 7]
```