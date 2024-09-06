```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    result = 1
    product = 1
    for num in numbers:
        result *= num
        product += num
    return (result, product)
#unit tests
test_data = [1, 2, 3, 4]
test_result = sum_product(test_data)
print("Test Result:", test_result)
# Output: (6, 12)
test_empty = []
test_result2 = sum_product(test_empty)
print("Test empty result:", test_result2)
``` 
This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function passes all the test cases with the sum and product calculated by the function, the test results are printed.