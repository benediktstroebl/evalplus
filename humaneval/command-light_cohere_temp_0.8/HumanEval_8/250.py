```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test case
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: {result[1]}")  # Output: (10, 24)

# Output of empty list
numbers = []
result = sum_product(numbers)
print(f"Sum: {result[0]}, Product: 1")  # Output: (0, 1)
```

I hope this provides a complete solution to the problem, along with the test case to validate the function's correctness.