```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until a given moment in the sequence.
    Each number in the max sequence up to the current maximum element. 
    Returns a needed maximum list with the corresponding index
    """
    result = [num for num, index in zip([max(numbers) for _ in range(len(numbers) + 1)] + [numbers[0]] if len(numbers) > 0), index < len(numbers))]
    return result

# Test case
numbers = [1, 2, 3, 4, 5]
test_result = rolling_max(numbers)
print(test_result)  # Output: [3, 4, 5, 5]
```