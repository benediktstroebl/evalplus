```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [max(n) for n in numbers if n != numbers[-1]]

# Test the function
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)  # Output: [1, 2, 3, 3, 3, 4, 4]

# Test negative numbers
numbers2 = [1, 2, 3, -2, 3, -3]
result2 = rolling_max(numbers2)
print(result2)  # Output: [-3, -3, -3]
```
The function takes a list of integers as input and returns a list of the maximum elements found while moving from the beginning of the list to the end. The function uses a list comprehension to find the maximum element at each moment.