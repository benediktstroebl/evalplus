```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_cases = [
    [], 0, 1,
    [1, 2, 3], (3, 6)
  ]

# Test execution summary
for test_case in test_cases:
    actual_sum, actual_product = sum_product(test_case)
    print(f"Test case: [{test_case}], Expected ({sum}, {product})")
    print(f"Actual: {actual_sum}, {actual_product}")
    print()
``` 
The provided Python code defines a function called sum_product that calculates the sum and product of a list of integers. 

It uses a for loop to iterate through the list, updating the running sum and product. 

The function then returns a tuple containing the calculated sum and product.

The code also includes a set of test cases, which are lists of integers. Each test case is passed to the sum_product function, and the results are printed to the console. 

This code demonstrates a basic implementation of calculating the sum and product of a list of integers using a loop.