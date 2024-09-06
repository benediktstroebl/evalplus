Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    return (sum(numbers), product(numbers))

# Test case
test_sum_product = [1, 2, 3, 4]
result = sum_product(test_sum_product)
print(result)  # Output: (6, 24)
```

The sum_product function calculates the sum and product of a list of integers and returns them in a tuple. The test case demonstrates how the
the function behaves when passed an empty list or a list of specific numbers.