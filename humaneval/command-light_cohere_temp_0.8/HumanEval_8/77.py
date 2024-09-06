```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    If the list is empty, return (0,1)
    If all the numbers in the list are equal, return (sum(numbers), 1)
    Otherwise, return (sum(numbers), product(numbers))
    """
    if not numbers:
        return (0, 1)
    if len(numbers) == 1:
        return (sum(numbers), numbers[0])
    sum_ = sum(numbers)
    prod_ = 1
    for x in numbers:
        prod_ = prod * x
    return (sum_, prod_)

# Unit tests
test_sum_product = []
test_sum_product.append([1, 2, 3, 4])
test_sum_product.append(5, 6)
test_sum_product.append(7, 8)
test_sum_product.append(9, 9)
test_sum_product.append([10, 11])
test_sum_product.append(12, 13, 14)
test_sum_product.append(15, 16, 17)

def test_function(*args):
    test_sum_product = sum_product(*args)
    print(f"Test Results: { sum: { test_sum_product[0], test_sum_product[1] })")

test_function(1, 2, 3, 4)
test_function(5, 6)
test_function(7, 8)
test_function(9, 9)
test_function(10, 11)
test_function(12, 13, 14)
test_function(15, 16, 17)
```