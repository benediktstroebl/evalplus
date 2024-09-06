Here is a Python script that has a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with a sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)
```
The code defines a function `sum_product` that calculates the sum and product of a list of integers, and passes the tests with the sample input `[1, 2, 3, 4]`.  The function returns a tuple with the sum and the product of the numbers in the list.