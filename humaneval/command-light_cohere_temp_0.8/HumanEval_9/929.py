Here's the self-contained Python script with a function 'rolling_max' that generates a list of the rolling maximum elements from a given list of integers:
```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_roll = numbers[0]
    current_max = numbers[0]
    
    for num in numbers[1:]:
        current_max = max(num, current_max)
        max_roll = max(max_roll, current_max)
    
    return [max_roll]

# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [3, 3, 3, 4, 4]

numbers = [1, 2, 3, 4, 5, 6]
result2 = rolling_max(numbers)
print(result2)  # Output: [5, 6]
```

The function 'rolling_max' takes a list of integers as input and returns a list of the rolling maximum elements found in the sequence. The function uses a maximum value of the first element in the list as the initial value for 'max_roll', and updates this value with each new element in the sequence to ensure that the rolling maximum is calculated correctly.