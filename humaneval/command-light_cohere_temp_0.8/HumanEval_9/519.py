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

# Test cases
numbers1 = [1, 2, 3, 4]
print(rolling_max(numbers1))  # Expected output: [1, 2, 3, 3, 3, 4, 4]

numbers2 = [10, 5, 6, 7]
print(rolling_max(numbers2))  # Expected output: [10, 10, 10, 7]

numbers3 = [100, 200, 300]
print(rolling_max(numbers3))  # Expected output: [100, 200, 300]
```
This script defines a function called **rolling_max** that takes a list of integers as input and returns a new list with the rolling maximum elements. The function initializes the constant max_so_far with the first element of the input list and then iterates over the remaining elements. It compares each element with the maximum so far and updates the constant with the larger value if a larger element is found.

The test cases provided are designed to validate the functionality of the rolling_max function. You can modify the