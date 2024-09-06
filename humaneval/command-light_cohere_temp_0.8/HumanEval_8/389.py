```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with edge cases and standard input
test_sum_product = [
    (), (0, 1)
    (1, 2, 3, 4), (10, 24)
    (5, 6, 7, 8), (100, 120)
]

result = sum_product(test_sum_product)

assert len(result) == 2
assert result[0] == 16
assert result[1] == 4160
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. It returns a test the test cases with the function using the `test_sum_product` list, which covers various scenarios, including edge cases and standard input.

The `sum_product` function is then tested against these cases, and the results are checked to match the expected output using assertions.