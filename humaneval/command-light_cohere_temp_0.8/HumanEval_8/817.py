```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test the function with a sample input
numbers = [1, 2, 3, 4]
result = sum_product(numbers)
print(result)  # Prints (6, 24)
```
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function takes a input as a list of integers and returns a tuple containing the sum and product of the numbers in the list. The code also provides a test of the function with a sample input, passing the expected output (6, 24) as an argument to the `sum_product` function.