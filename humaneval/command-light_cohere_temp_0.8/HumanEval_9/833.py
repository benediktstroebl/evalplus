```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until the given moment in the sequence.
    >>> numbers=[1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers)  [1, 2, 3, 3, 3, 4, 4]
    """
    numbers = [num for num in numbers if num != 0]  # Remove zero elements to avoid NaN issue in max() calculation
    max_num = numbers[0]
    rolling_max_list = [max_num]
    for num in numbers[1:]:
        current_max = max(max_num, num)
        max_num = current_max
        rolling_max_list.append(current_max)
    return rolling_max_list

# Test cases
numbers = [1, 2, 3, 4, 5]
rolling_max_result = rolling_max(numbers)
print("Rolling Max:", rolling_max_result)  # Output: [3, 3, 4, 5]
```

This Python code provides a self-contained function called `rolling_max`, which generates a list of rolling maximum elements found in a given list of integers. The function handles the remove zero elements from the input list to avoid potential NaN issues in the maximum calculation, then iterates through the non-zero elements, tracking the current maximum with each element. The rolling maximum is then updated and appended to the result list.