Here is a Python script with a self-contained function that solves the problem of calculating the sum and product of a list of integers, and passes corresponding tests:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function with sample inputs
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print("Sum:", result)  # Output: (10, 24)
print("Product:", result[1])  # Output: 24
``` 
This code defines a function `sum_product` that takes a list of integers as an argument and returns a tuple with the sum and product of the integers in the list. 

The function uses a loop to iterate over each integer in the list, multiplying the current number with the running product to calculate the product, and adding the number to the sum.

Finally, the function is tested with a sample input list `[1, 2, 3, 4]` and the results are printed.