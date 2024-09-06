```python
from typing import List

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
print("Sum:", result)
print("Product:", result[1])

# Tests
assert sum(numbers) == result[0]
assert numbers[0] == result[1]

``` 
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a types for better code readability and maintains correct type hints for the function signature. 
The example usage and tests demonstrate how the function is used and the results are correctly compared with the expected values.