```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)
# Test the function with valid inputs and validate the expected output
test_valid_input = [1, 2, 3, 4]
test_invalid_input = []
test_result = sum_product(test_valid_input)
test_result_err = sum_product(test_invalid_input)

# Validate the function's output by comparing against the expected results
assertEqual(test_result, (10, 24))
assertEqual(test_result_err, (0, 1))
 ``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers, then validates it using `unittest` with the `assertEqual` function. The test cases are designed to cover scenarios with both valid and invalid inputs, passing them through the `sum_product` function to catch any potential errors or unexpected outputs.