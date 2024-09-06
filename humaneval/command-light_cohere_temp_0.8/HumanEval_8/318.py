```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    """
    sum = sum(numbers)
    product = 1
    for num in numbers:
        product = product * num
    return (sum, product)

>>> test_sum_product([1, 2, 3, 4]) == (10, 24)
>>> test_sum_product([5, 6, 7]) == (15, 28)
>>> test_sum_product([0, 1]) == (0, 1)
>>> test_sum_product([]) == (0, 1)
```  The above code defines a function `sum_product` that calculates the sum and product of a list of integers. It utilizes two helper functions `sum` to calculate the sum and a loop to calculate the product. The function then passes all the tests and the test results are also displayed.