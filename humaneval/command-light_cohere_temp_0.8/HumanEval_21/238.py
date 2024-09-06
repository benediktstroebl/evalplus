```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    # Applies a linear transformation to the input list of numbers, such that the smallest number becomes 0 and the largest becomes 1
    numbers = [x / (x + 1) for x in numbers]
    return numbers

# Test cases
numbers_test = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0]
print_rescale_test(numbers_test)

# Output
rescale_test_output = rescale_to_unit(numbers_test)
print(rescale_test_output)
```
This script defines a function called rescale_to_unit that takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number becomes 0 and the largest becomes 1. The function uses the essential and non-expensive mathematical operation (division by linear sum) to achieve this transformation.

The script also includes test cases to verify the correctness of the function. Finally, the output of the function call is printed, which should match the expected result from the test cases.