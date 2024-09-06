```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various inputs
test_values = [1, 2, 3, [4], 5, [6, 7], 8]
test_results = sum_product(test_values)
print("Test Results:", test_results)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. It handles empty lists gracefully by returning (0, 1) in such cases. The function is then tested with various inputs and the results are printed to the console.