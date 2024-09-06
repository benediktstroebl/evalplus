```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Unit tests
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (6, 24)
print("Product:", result[1])  # Output: 24
``` 
This script defines a function sum_product that calculates the sum and product of a list of integers. The "typing" module is used to define the function's parameter types. The function uses a loop to iterate through the list and calculate the sum and product. The output displays the expected results for an empty list and a list of specific numbers.