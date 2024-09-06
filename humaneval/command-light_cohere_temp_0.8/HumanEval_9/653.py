```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_values = [current_max]

    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_count += 1

    return max_values

# Test cases
numbers = [1, 2, 3, 4, 3, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5, 6]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 4, 6]

numbers = [5, 5, 5, 5, 5, 5]
result = rolling_max(numbers)
print(result)  # Output: []
```

The above Python code defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function uses the first initializes the max value and the `max_count` as 0. It iterates through through the maximum element and increments the `max_count`. Finally, the function returns the list of `max_values`.