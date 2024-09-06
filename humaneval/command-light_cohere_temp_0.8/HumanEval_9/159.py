```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.append(numbers[-1])  # Add the last element to the list for comparison
    max_numbers = [num for num in numbers if num > numbers[-1]]
    return max_numbers

# Test the function
test_rolling_max = []
test_rolling_max.append([1, 2, 3, 2, 3, 4, 2])
test_rolling_max.append([1, 2, 3, 3, 3, 3, 4, 4])

print(rolling_max(test_rolling_max))
```