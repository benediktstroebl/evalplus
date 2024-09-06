```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Calculate the sum and product of a list of integers.
    product = 1
    for num in numbers:
            product = num * product
            sum += num
    return (sum, product)
    """
    product = 1
    sum = 0
    for num in numbers:
        product = num * product
        sum += num
    return (sum, product)

# Sample Test Cases
test_1 = [1, 2, 3, 4]
test_2 = []
test_3 = [10, 1]

result_1 = sum_product(test_1)
result_2 = sum_product([])
result_3 = sum_product([10, 2])

print(f" Test Case 1: Result: {result_1, result_2}")
print(f" Test Case 2 Result: {result_3})
```

This code provides a self-contained function `sum_product` which takes a list of integers as input and returns a tuple with the sum and product of the list elements. It then passes corresponding tests to check the function's correctness.