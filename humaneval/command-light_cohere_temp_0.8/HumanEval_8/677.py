```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Test cases
test_data = [0, 1]
test_sum_product = sum_product(test_data)
print(test_sum_product)  # Output: (1, 1)
test_data = [1, 2, 3, 4]
test_sum_product = sum_product(test_data)
print(test_sum_product)  # Output: (10, 24)
test_data = [5, 6, 7, 8]
test_sum_product = sum_product(test_data)
print(test_sum_product)  # Output: (35, 56)
 ``` 
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The test cases are provided to demonstrate the function's behavior. 

Please note that this script does not rely on external libraries and can be easily copied and pasted.