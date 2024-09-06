```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with various inputs
test_case = [1, 2, 3, 4]
result = sum_product(test_case)
print(f"Sum: {result[0]}  , Product: {result[1]}")

test_case = []
result = sum_product(test_case)
print(f"Sum: {result[0]}  , Product: 1")

test_case = [1, 2, 3]
result = sum_product([1, 4, 5])
print(f"Sum: {result[0]}  , Product: {result[1]}")
```
This code defines a function called sum_product that takes a list of integers as input and returns a tuple containing their sum and product. The product is initialized to 1, and the sum is calculated by iterating through the input list and adding each element to the sum. The test_case variable is assigned a list of integers, and the sum_product function is called with this list. The function returns the result, and the sum and product are printed to the console.