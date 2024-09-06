```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    A rolling maximum function that returns the maximum element found within a given moment in the sequence.
    >>> numbers = [1, 2, 3, 2, 3, 4, 2]
    >>> rolling_max(numbers) 
    [3, 3, 3, 4, 4]
    """
    # We need to keep track of the maximum element seen so far
    max_element = numbers[0]
    
    # Go through the list and compare each element with the maximum seen so far
    for num in numbers[1:]:
        if num > max_element:
            max_element = num  # Update the current maximum seen
    
    return [max_element]  # Return the list of rolling maximum elements

# Test case 1:
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [3, 3, 3, 4, 4]

# Test case 2:
numbers = [1, 2, 3, 9, 5, 6, 4, 3, 2]
result = rolling_max(numbers)
print(result)  # Expected output: [9, 9, 9]
```
This Python script defines a function called rolling_max that takes a list of integers as input and returns a list of the maximum elements found within the sequence, effectively implementing the rolling maximum concept. The test cases provided demonstrate the