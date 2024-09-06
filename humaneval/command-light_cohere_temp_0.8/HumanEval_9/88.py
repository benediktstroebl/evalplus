```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = [int(i) for i in numbers]  # Convert input list to integer array
    return [max(numbers[i:]) for i in range(len(numbers))]]

# Test case 1
test_case_1 = [1, 2, 3, 4, 5]
result_case_1 = rolling_max(test_case_1)
assert len(result_case_1) == 5
assert result_case_1 == [5, 4, 3, 2, 1]

# Test case 2
test_case_2 = [1, 2, 4, 3, 7]
result_case_2 = rolling_max(test_case_2)
assert len(result_case_2) == 5
assert result_case_2 == [7, 6, 5, 4, 3]

# Test case 3
test_case_3 = [2, 3, 2, 1, 5]
result_case_3 = rolling_max(test_case_3)
assert len(result_case_3) == 5
assert result_case_3 == [5, 4, 3, 2, 1]

print("All tests passed!")
```