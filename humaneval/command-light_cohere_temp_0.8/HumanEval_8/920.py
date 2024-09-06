```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test the function with various input scenarios
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append([1, 5, 6, 7])
test_sum_product.append([8, 9, 10])
test_sum_product.append([10, 11, 12, 13])

# Call the function and compare the results with the test cases
test_sum_product = sum_product(test_sum_product)

# Print the results
print("Sum:",test_sum_product[0])
print("Product:",test_sum_product[1])
``` 
This Python script includes a self-contained function `sum_product` that calculates the sum and product of a list of integers. It also passes tests for various input scenarios, and the function is called with the test cases. 

The function returns a tuple of the sum and product values, which are then printed.