```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers = list(sorted(numbers))  # sort the list in ascending order
    return [x for x in numbers if x == numbers[0]]  # return the first occurrence of the maximum element

# Test case 1: Verify function
test_case1 = [1, 3, 2, 4, 3, 5]
result1 = rolling_max(test_case1)
assert result1 == [5, 4, 3, 3, 2], "Error in function: " + "expected: " + [5, 4, 3, 3, 2] + ", but got: " + str(result1)

# Test case 2: Verify that it works with negative numbers too
test_case2 = [-1, -2, -3, -4, -5]
result2 = rolling_max(test_case2)
assert result2 == [ -5, -4, -3, -3 ], "Error in function with negative numbers: " + str(result2)

# Test case 3: Verify that it works with mixed numbers
test_case3 = [2.5, 2. .5, 3.5, 4.5, 3]
5, 2.5, 4, 5]
result3 = rolling_max(test_case3)
assert result3 == [4, 5, 2.5, 2, 2], "Error in function with mixed numbers: " + str(result3)

print("Test cases passed")
```