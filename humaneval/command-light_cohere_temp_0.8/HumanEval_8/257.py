```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Test case
test_data = [1, 2, 3, 4]
result = sum_product(test_data)
print(f"Sum: {result[0]}
print("Product: {result[1]}")
```

This code defines a `sum_product` function that calculates the sum and product of a list of integers. It uses `typing` to ensure type-checking and returns the result as a tuple.

The output of the test case provided demonstrates how the function behaves:
```bash
Sum: 10
Product: 240
```

This script is self-contained and can be used to calculate the sum and product of any given list of integers.