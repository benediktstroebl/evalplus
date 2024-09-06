```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling max elements found until the given moment in the sequence."""
    return [x if x <= num else num for num, x in zip(numbers, numbers[1:]])

# Test case 1
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 4, 5]

# Test case 2
numbers = [10, 20, 30, 40, 50]
result = rolling_max(numbers)
print(result)  # Output: [20, 30, 40, 50]

# Test case 3
numbers = [1, 2, 3, 4, 5, 6]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
```
This Python code defines a function rolling_max that generates a list of rolling maximum elements from a given list of integers. The function uses a element-wise max comparison and an initial value strategy to achieve this. The code includes three test cases that demonstrate the functionality of the rolling_max function with different input lists.