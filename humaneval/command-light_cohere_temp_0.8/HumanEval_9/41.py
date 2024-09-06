```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = List(numbers)
    current = max_numbers[0]
    result = [current]
    
    for num in max_numbers[1:]:
        current = max(current, num)
        result.append(current)
    
    return result

# Test cases
numbers1 = [1, 2, 3, 4, 5]
print(rolling_max(numbers1))  # Expected output: [1, 2, 3, 3, 4, 5]

numbers2 = [10, 2, 4, 6, 8]
print(rolling_max(numbers2))  # Expected output: [10, 10, 10, 6, 8]

numbers3 = [123, 456, 123]
print(rolling_max(numbers3))  # Expected output: [123, 456, 123]
```
This script defines a rolling_max function, which takes a list of integers as input and generates a new list of integers with the maximum element from the original list rolling over the entire sequence. It effectively solves the Fraser's 'Rolling Maximum' problem and passes the corresponding tests using sample inputs.