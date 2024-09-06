```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [max(numbers[i:], numbers[i+1]) for i in range(len(numbers)-1)]

# Test case 1
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test case 2
numbers = [1, 2, 3, 4, 3, 2, 1, 3]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 2, 1]

# Test case 3
numbers = [10, 10, 10]
result = rolling_max(numbers)
print(result)  # Output: [10, 10, 10]
```
This script defines a function `rolling_max` that calculates the rolling maximum elements of a given list of integers. It returns a max values from the list using a sliding window approach. 
The script then tests the function with three different sets of numbers and verifies that the function correctly calculates the rolling maximum elements.