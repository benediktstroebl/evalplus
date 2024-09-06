```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [num for num, i in zip(numbers, range(len(numbers))) if i == numbers.max]
``` 
# Test case using a list of integers
test_cases = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6, 7],
    [10, 20, 30, 40],
    [100, 200, 300]
]

# Call the function and compare the output with expected results
for test_data, expected_results in zip(test_cases, rolling_max(test_cases)):
    assert list(set(test_data)) == set(expected_results), "The rolling maximum function doesn't return the expected results."
```