```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)
# Testing the function with different inputs
test_list = [1, 2, 3, 4, 5]
test_sum_product = sum_product(test_list)
print("Test Sum Product:", test_sum_product)
test_single_value = (10, 1)
print("Test Single Value:", test_single_value)
``` 
This code provides a self-contained function that takes a list of integers, calculates their sum and product, and passes the results. 

This approach allows you to solve the problem in a more compact and structured way.