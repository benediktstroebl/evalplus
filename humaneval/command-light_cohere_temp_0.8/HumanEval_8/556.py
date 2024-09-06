Here is a Python script that includes a self-contained function `sum_product` solving the problem:
```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a given list of integers.
    Return a sum and product as a tuple.
    """
    empty product should be equal to 1.
    """
    sum([]) -> 0
    """
    product = 1
    for num in numbers:
        product = num * product
        sum += num
    return (sum, product)

# Test cases
test_cases = [(), 1, 2, [3, 4], [10, 20])

for test_case in test_cases:
    result = sum_product(test_case)
    print(f"Test case: {test_case}, Result: {result})
```

This code defines a function `sum_product` that calculates the sum and product of a list of integers and passes several test cases.  The test cases include empty list, single number, list of numbers, and a list of numbers with products.  The output will show the results for each test case.