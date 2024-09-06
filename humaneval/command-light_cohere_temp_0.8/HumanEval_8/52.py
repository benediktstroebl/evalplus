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
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. 

The function takes a list of integers as input and iterates through the list, calculating the product by multiplying the elements and then adding them to calculate the sum.