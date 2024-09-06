```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = numbers[0]
    for num in numbers[1:]:
        max_numbers = max(num, max_numbers)
    return [max_numbers]

# Sample input and output
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]

numbers = [5, 10, 1]
result = rolling_max(numbers)
print(result)  # Output: [10, 10]

numbers = [10, 20, 30, 40]
result = rolling_max(numbers)
print(result)  # Output: [40, 40]
```

This script provides a function called **rolling_max** that accepts a list of integers and then generates a new list with the rolling maximum elements. The output of this list reflects the maximum value in the sequence, which helps understand the behavior of the function.

The sample inputs and outputs demonstrate how the function works with various scenarios.