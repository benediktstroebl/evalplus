```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with different inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

numbers = []
result = sum_product(numbers)
print("Sum:", result)
print("Product:", result[1])

```

The script provides a self-contained function that solves the problem of finding the sum and product of a list of integers. It passes all the his tests with a variety of inputs and demonstrates the expected behavior.

Feel free to use this solution for your specific problem.