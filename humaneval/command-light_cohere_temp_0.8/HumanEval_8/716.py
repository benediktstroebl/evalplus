Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:

```python
from typing import List, Tuple
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    : RETURN: (sum(numbers), product(numbers))
    """
    product = 1
    sum = 0
    for num in numbers:
        sum += num
        product *= num
    return (sum, product)

# Test cases
test_sum_product_list = [5, 2, 10, 3]
test_sum_product_result = sum_product(test_sum_product_list)
print("Test 1 sum:", test_sum_product_result)
print("Test 1 product:", test_sum_product_result)
test_empty_list = []
test_sum_product_empty_list = sum_product(test_empty_list)
print("Test 2 sum:", test_sum_product_empty_list)
print("Test 2 product:", test_sum_product_empty_list)
test_single_element = [10]
test_sum_product_single_element = sum_product(test_single_element)
print("Test 3 sum:", test_sum_product_single_element)
print("Test 3 product:", test_sum_product_single_element)
test_large_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_sum_product_large_list = sum_product(test_large_list)
print("Test 4 sum:", test_sum_product_large_list)
print("Test 4 product:", test_sum_product_large_list)
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers. The function returns a value as a tuple of both the sum and product. 

Test cases are provided to verify the correctness of the `sum_product` function. The test results are printed out to the console.