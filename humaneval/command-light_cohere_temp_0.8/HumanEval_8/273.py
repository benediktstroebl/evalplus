```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function with a list of integers
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result[0])  # Output: 10
print("Product:", result[1])  # Output: 24
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The `typing` module is also imported, which brings in type hints and other functionality. 
In the test section, a list of integers `[1, 2, 3, 4]` is passed to the `sum_product` function, and the results are printed, demonstrating the function's expected behavior.