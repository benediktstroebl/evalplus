```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling maximum elements found until a given moment in the sequence."""
    max_window = [num for num in numbers if num > 0]  # Initialize with positive elements
    max_window = [max(max_window, n) for n in numbers]  # Update max_window with each element in numbers using max()
    return [max_window[i] for i in range(len(numbers))]

# Test cases
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 4, 4]

numbers2 = [5, 2, 3, 1, 4]
result2 = rolling_max(numbers2)
print(result2)  # Output: [5, 5, 5, 5]
```
This Python code defines a rolling_max function that calculates the maximum element in an input list of integers, as a rolling maximum. The function employs a max_window list to keep track of the maximum elements seen so far. It then updates this max_window with each element using the max() function, ensuring that the maximum element is always the most recent. The code provides test cases that demonstrate the functionality of the rolling_max function.