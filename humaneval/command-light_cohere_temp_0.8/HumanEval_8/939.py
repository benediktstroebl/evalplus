```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test case function
def test():
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    print("Sum:", result)
    print("Product:", result[1])
    return_value = result
    print("Return value:", return_value)
test()  # Function call
```
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function iterates through a list, calculates the product as 1 and updates the running sum. The test case function demonstrates the test case by passing the list `[1, 2, 3, 4]` to the `sum_product` function. The function then returns a tuple of the sum and product of the numbers in the list.

This code demonstrates the implementation and usage of the function to calculate the sum and product of a given list of integers.