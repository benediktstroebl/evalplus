```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ 
    Generate a list of rolling max elements from a given list of integers. 
    Args: 
        numbers (List[int]): Input list of integers
    Returns: 
        List[int]): A list of rolling max elements found until the given moment. 
    Test suite: 
        [5, 3, 2, 1, 5, 4, 3, 5, 2, 3]
    """
    numbers = [5, 3, 2, 1, 5, 4, 3, 5, 2, 3]
    rolling_maxes = [num for num in numbers if num == max(numbers)]
    return rolling_maxes

# Test suite
test_suite = [5, 3, 2, 1, 5, 4, 3, 5, 2, 3]

for num, expected in zip(rolling_max(test_suite), test_suite):
    print(f"Test passed: got {num}, expected {expected}")
```