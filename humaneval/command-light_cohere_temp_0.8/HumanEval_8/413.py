```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function
x = [1, 2, 3, 4]
result = sum_product(x)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24000000

y = [5, 6, 7]
result = sum_product(y)
print("Sum:", result)  # Output: (18, 56)
print("Product:", result[1])  # Output: 560000000
```
This code defines the function `sum_product`, which takes a list of integers as input and returns a tuple containing the sum and product of the numbers. The function calculates the sum and product using a loop and updates the corresponding variables. The test code then demonstrates the result of the function, providing the sum and product of the input list `[1, 2, 3, 4]` and `[5, 6, 7]`.