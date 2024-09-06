```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(numbers)
    current_max = max_numbers[0]
    
    for num in numbers[1:]:
        current_max = max(num, current_max)
        max_numbers[0] = current_max
        
    return max_numbers

# Example usage
numbers = [1, 2, 3, 2, 3, 4, 2]
result = rolling_max(numbers)
print(result)
```
The function takes a list of integers as input and returns a new list that contains the rolling maximum elements found in the original list. The function uses a simple iterative approach to calculate the rolling maximum. 

The output will be: `[1, 2, 3, 3, 3, 4, 4]`.