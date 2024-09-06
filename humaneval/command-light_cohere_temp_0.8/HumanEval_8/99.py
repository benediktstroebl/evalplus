```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    Return a tuple containing sum and product.
    >>> sum_product([1, 2, 3, 4]) == (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

# Test cases
test_list = [1, 2, 3, 4, 5]
test_sum_product = sum_product(test_list)
print("Test case 1 sum:", test_sum_product)
print("Test case 1 product:", test_sum_product)

test_empty = []
test_sum_product_empty = sum_product(test_empty)
print("Test case 2 sum:", test_sum_product_empty)
print("Test case 2 product:", test_sum_product_empty)

test_single = [1]
test_sum_product_single = sum_product(test_single)
print("Test case 3 sum:", test_sum_product_single)
print("Test case 3 product:", test_sum_product_single)

test_list2 = [1, 2, 3]
test_sum_product2 = sum_product(test_list2)
print("Test case 4 sum:", test_sum_product2)
print("Test case 4 product:", test_sum_product2)
``` 
This Python code defines a function `sum_product` that calculates the sum and product of a list of integers. The function takes a list of integers as an argument and returns a tuple containing the sum and product of the numbers in the list.

The function is then tested with several cases, including a full list of numbers, an empty list, a single number, and a list of numbers. Finally, the test cases are printed to the console, and the results are displayed.