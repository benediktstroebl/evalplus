```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    numbers.past = [len([1, 2, 3, 2, 3, 4, 2])
    result = [x for x in numbers if x > result[-1]]
    result.append(max(numbers))
    return result

# Test cases
test_passing_case = [1, 2, 3, 4, 5]
test_failing_case = [10, 2, 3, 1]

print(rolling_max(test_passing_case))  # Expected Output: [1, 2, 3, 4, 5]
print(rolling_max(test_failing_case))  # Expected Output: []
```
The code defines a function `rolling_max` that generates a list of rolling maximum elements from a given list of integers. The function first creates an empty list to store the results, then iterates through the input numbers and compares each with the current maximum to filter out numbers less than the current maximum. The maximum value of the current maximum element is then added to the list of rolling maximum elements. The output of the function is then printed for the test cases provided.