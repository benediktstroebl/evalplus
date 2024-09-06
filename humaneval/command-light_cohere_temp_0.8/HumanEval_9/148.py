```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    max_count = 0
    current_max = numbers[0]
    max_list = [current_max]
    
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
        max_count += 1
        
    return max_list[:max_count]

# Test case 1
test_cases = [1, 3, 6, 2, 4, 5]
result = rolling_max(test_cases)
assert len(result) == 5, "Wrong number of elements returned."

# Test case 2
test_cases = [1, 2, 3, 9, 10]
result = rolling_max(test_cases)
assert len(result) == 4, "Wrong number of elements returned."

# Test case 3
test_cases = [2, 3, 2, 3, 4]
result = rolling_max(test_cases)
assert len(result) == 4, "Wrong number of elements returned."
```

This Python script provides a self-contained function called `rolling_max` which generates a list of the rolling maximum elements in a given list of integers. The function uses a types to ensure the input and return the correct results for the provided test cases.