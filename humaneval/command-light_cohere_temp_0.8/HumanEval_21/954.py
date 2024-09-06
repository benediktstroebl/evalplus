```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transformation to the input list
    numbers_res = [x / (x + 1) for x in numbers]
    return numbers_res

# Test cases
test_cases = [
    [0.0, 2.0, 3.0, 4.0, 0.0],
   0.5, 0.0, 0.0],
   0.75, 1.0
]

# Test results
test_results = rescale_to_unit(test_cases)

# Print test results
print(test_results)
```

In this solution, the `rescale_to_unit` function accepts a list of numbers and returns a new list where each element has been scaled to the range [0,1]. The test cases are defined as a list of test values, and the `rescale_to_unit` function is called with those test values. The resulting test results are stored in the `test_results` variable, which is then printed to the console.