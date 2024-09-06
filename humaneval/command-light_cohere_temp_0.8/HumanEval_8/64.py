```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Example usage
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(f"Sum: {result[0]}")
print(f"Product: {result[1]}")
``` 
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. 

It uses a loop to iterate through the list, updating a running product and sum. The product is then 1, and the sum is calculated by adding each integer in the list. 

The script then demonstrates the usage of the `sum_product` function by passing a list of integers `[1, 2, 3, 4]` and printing the result, which should be (10, 24). 

This is a simple example that demonstrates how to define and use a self-contained function with the `sum_product` and `List` types.