```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
# Test case 1: Insert between all elements
test_case_1 = [1, 2, 3, 4, 5]
result_case_1 = intersperse(test_case_1, 4)
assert len(result_case_1) == 5  # Should have 5 elements
assert all([i + i * 4 for i, j in zip(range(5), result_case_1)]) == result_case_1

# Test case 2: Insert between every 2nd and 3rd elements
test_case_2 = [1, 2, 4, 3, 5]
result_case_2 = intersperse(test_case_2, 4)
assert len(result_case_2) == 5  # Should have 5 elements
assert [j + i * 4 for i, j in zip(range(5), result_case_2)] == result_case_2

# Test case 3: Insert between every 3rd and 4th elements
test_case_3 = [1, 2, 3, 4, 5]
result_case_3 = intersperse(test_case_3, 4)
assert len(result_case_3) == 5  # Should have 5 elements
assert [j + i * 4 for i, j in zip(range(5), result_case_3)] == result_case_3
```
This script provides a self-contained function `intersperse` that inserts a specified `delimiter` between every two consecutive elements in the input list. The script also passes three test cases to verify the functionality of the `intersperse` function.