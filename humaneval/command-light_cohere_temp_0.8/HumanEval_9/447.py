```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    result = [max_so_far]
    
    for num in numbers[1:]:
        if num > max_so_far:
            max_so_far = num
        result.append(max_so_far)
    
    return result

# Test the function with sample inputs and verify the results
numbers = [1, 2, 3, 2, 3, 4, 2]
print(rolling_max(numbers))  # Output: [1, 2, 3, 3, 3, 4, 4]
```
The function rolling_max takes a list of integers as input and returns a list of the maximum elements found in the sequence so far, effectively calculating the rolling maximum. This function uses a technique of initializing the variable max_so_far with the first element of the sequence and then compares each subsequent element with the current maximum, updating the maximum whenever a larger value is encountered. The final result is a list of the maximum elements in the sequence.