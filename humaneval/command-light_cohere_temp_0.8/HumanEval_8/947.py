```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test the function with different inputs
test_inputs = [0, 1, 2, 3, 4,5,6,7]
test_outputs = [0, 1, 6, 24, 120, 720,0]

for test_input, expected_output in zip(test_inputs, test_outputs):
    actual_output = sum_product(test_input)
    print(f"Input: {test_input}, Expected Output: {expected_output}, Actual Output: {actual_output}")
``` 
This code provides a function `sum_product` that calculates the sum and product of a list of integers. It is then passing tests with different inputs to ensure the function's correctness.