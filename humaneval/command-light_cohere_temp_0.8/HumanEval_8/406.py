```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 0
    product = 1
    for num in numbers:
        result += num
        product *= num
    return (result, product)

# Test the function with various inputs
numbers1 = [1, 2, 3]
numbers2 = [3, 4, 5]
result1, product1 = sum_product(numbers1)
result2, product2 = sum_product(numbers2)

print("Test 1: Result =", result1, "and Product =", product1)
print("Test 2: Result =", result2, "and Product =", product2)
```
This code defines a function `sum_product` that takes a list of integers as input and returns a tuple of their sum and product. The function then calculates the product by iterating through each element in the list, while summing the numbers by adding each element. The tests are then performed on the function, and the results are printed out.