```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a list of integers.
    >>> return sum_product([1, 2, 3, 4])
    (10, 24)
    """
    product = 1
    sum = 0
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#Unit tests
test_sum_product = []
test_sum_product.add([range(0, 5))
test_sum_product.add((1, 2, 3, 4))
test_sum_product.add(5, 5)

test_sum_product = [test_sum_product[i] + test_sum_product[i+1] for i in range(0, len(test_sum_product)-1)]

print(sum_product(test_sum_product))
```