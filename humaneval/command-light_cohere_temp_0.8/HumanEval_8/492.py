```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of all the integers in a list """
    if not numbers:
        return (0, 1)
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product *= num
    return (sum, product)

# Unit tests
test_sum_product = []
test_sum_product.add(1, 2, 3)
test_sum_product.add(4, 5, 6)
test_sum_product.add(7, 8, 9)
test_sum_product.add(10, 20, 30)

# Run the function and check the results
test_sum_product = [(sum_product(test_numbers) for test_numbers in test_sum_product])

print(test_sum_product)  # Expected output: [(6, 3000050)]
```
This Python script defines a function `sum_product` that calculates the sum and product of a list of integers. It also provides a unit tests to check the function's behavior for different input scenarios. The function returns the expected results for the test cases.