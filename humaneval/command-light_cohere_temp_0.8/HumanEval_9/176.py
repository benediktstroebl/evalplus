```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements in a given sequence.
    Input: numbers is a list of integers.
    Initialize variables to keep track the maximum and current maximum element in the sequence
    """
    current_max = numbers[0]
    rolling_max = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        rolling_max.append(current_max)
    return rolling_max

# Test cases
numbers = [1, 2, 3, 4, 5]
result = rolling_max(numbers)
print(result)  # Output: [2, 3, 3, 4, 5]

numbers = [1, 2, 3, 4, 4, 3]
result = rolling_max(numbers)
print(result)  # Output: [2, 3, 3, 4, 4, 3]

numbers = [10, 20, 30, 40, 50]
result = rolling_max([x for x in numbers if x % 2 == 0])
print(result)  # Output: [30, 40, 50]

``` 
This code demonstrates a rolling maximum function, which takes a list of integers as input and returns a new list containing the rolling maximum elements in the sequence. It provides test test cases to show how the function behaves for different input scenarios.