```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling maximum elements found until a given moment
    in the sequence.
    Test case: 
    1) All numbers are positive 
    2) There are enough elements to calculate rolling max. 
    3) The rolling max should be a list of increasing numbers
    """
    assert all(numbers) and len(numbers) >= 4, "Not enough positive numbers"
    assert len(numbers) == len(set(numbers)), "Numbers should be unique"

    # Calculate rolling max
    max_numbers = [num for num in numbers[-1:] + numbers[-2:] + numbers[-3:] + numbers[:-2] if num >= max_numbers[-1]]

    return max_numbers
```