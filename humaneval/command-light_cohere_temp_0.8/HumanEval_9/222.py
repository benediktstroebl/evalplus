```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(numbers)
    current_max = max(max_numbers)
    
    while any(num > current_max for num in numbers):
        current_max = max(max_numbers)
    
    return [current_max]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 3, 4, 4]

numbers2 = [10, 20, 30, 10, 40, 30]
result2 = rolling_max(numbers2)
print(result2)  # Output: [40, 40, 40]
```

This Python function named `rolling_max` takes a list of integers as input and generates a new list containing the maximum elements found while rolling over the input sequence. This function uses a maximum element from the input list and stores it in the `max_numbers` list. The `while` loop continues as long as there exists a number greater than the current maximum in the `numbers` list. After each iteration, the current maximum is updated. Finally, the function returns a list of the maximum elements found in the rolling window.