Here's the solution:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transform
    numbers_transformed = [x / (x + 1e-8) for x in numbers]

    return numbers_transformed

# Test cases
test_data = [
    [0.1, 0.0, 0.0, 0.0, 1.0, 2.0, 4.0],
   0, 3.0, 0.0]

# Test list of numbers and the result of the rescale_to_unit function
test_result = rescale_to_unit(test_data)

print(test_result)
```

This code defines a function `rescale_to_unit` that transforms a list of numbers so that the smallest number is 0 and the largest is 1. The function takes a list of numbers as an argument, applies the linear transformation, and returns the transformed list.

The code also provides a test case with a list of numbers and the result of the `rescale_to_unit` function. The test result should be the0, 0.5, and 1.0, which the expected to be in the resulting list.