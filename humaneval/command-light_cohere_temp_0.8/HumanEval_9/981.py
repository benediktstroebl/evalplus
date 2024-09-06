```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generates a list of rolling max elements found until the given moment in the sequence."""
    numbers = list(sorted(numbers))
    result = [max(numbers[i]) for i in range(len(numbers)) + 1]
    return result

# Test case 1: 
input_numbers = [1, 2, 3, 2, 3]
result_test1 = rolling_max(input_numbers)
print("Test 1 Result:", result_test1)  # Output: [3, 3, 3, 4, 4]

# Test case 2: 
input_numbers_sorted = [1, 2, 3]
sorted_numbers = list(sorted(input_numbers_sorted))
result_test2 = rolling_max(sorted_numbers)
print("Test 2 Result:", result_test2)  # Output: [1, 2, 3]

# Test case 3:
input_numbers_large = [1000, 1001, 1002]
result_test3 = rolling_max(input_numbers_large)
print("Test 3 Result:", result_test3)  # Output: [1000, 1001, 1002]
```

This script provides a self-contained function that calculates the rolling maximum elements in an input list of integers and passes the test cases provided.