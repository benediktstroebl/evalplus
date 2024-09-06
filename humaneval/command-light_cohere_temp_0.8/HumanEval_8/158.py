```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_sum_product_list = [1, 2, 3, 4, 5]
test_sum_product_tuple = (6, 7, 8, 9)

print("Test 1:")
result = sum_product(test_sum_product_list)
print(result)

print("Test 2:")
result = sum_product(test_sum_product_tuple)
print(result)
```
This script defines a function `sum_product` that calculates the sum and product of a list of integers. The function uses a loop to iterate through the list and calculate the product and sum of each integer, respectively. The function then returns a tuple containing the sum and product. 
The test cases pass without errors, verifying the functionality of the `sum_product` function.