Here is a self-contained Python script with a function that solves the problem of calculating the sum and product of a list of integers:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function
test_list = [1, 2, 3, 4, 5]
result = sum_product(test_list)
print(f"Sum: {result[0]}
print("Product: {result[1]}")
```
This script defines a `sum_product` function that takes a list of integers as an argument and returns a tuple containing the sum and product of the numbers in the list. The script then passes a test case with a list of integers [1, 2, 3, 4, 5], and prints both the sum and the product.