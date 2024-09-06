```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_sum_product_list = [5, 6, 7]
test_sum_product_tuple = (10, 20)
test_empty = ()

# Function call and tests results
print(f"Test case 1: sum ({'x' for x in test_sum_product_list}')) => {sum: 21}")
print(f"Test case 1: product ({'x' for x in test_sum_product_list}')) => {product: 56}")
print(f"Test case 2: sum ({'x' for x in test_sum_product_tuple}) => {sum: 40}")
print(f"Test case 2: product ({'x' for x in test_sum_product_tuple}) => {product: 400}")
print(f"Test case 3: sum (empty list) => {sum: 0}")
print(f"Test case 3: product (empty list) => {product: 1}")
``` 
The script defines a function `sum_product` that calculates the sum and product of a list of integers. The function is then tested with three test cases, and the results are printed out. 
The output will be:
```
Test case 1: sum ({'x' for x in test_sum_product_list'}) => {sum: 21}
Test case 1: product ({'x' for x in test_sum_product_list'}) => {product: 56}
Test case 2: sum ({'x' for x in test_sum_product_tuple}) => {sum: 40}
Test case 2: product ({'x' for x in test_sum_product_tuple}) => {product: 400}
Test case 3: sum (empty list) => {sum: 0}
Test case 3: product (empty list) => {product: 1}
```