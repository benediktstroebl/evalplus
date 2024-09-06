```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in a list """
    result = (sum(numbers), product(numbers))
    return result

#unit tests
test_sum_product = []
test_sum_product.add([range(1,10)]
test_sum_product.add([1, 1, 1)
test_sum_product.add(1, [1,2])
test_sum_product.add([1, 2, [3, 4])
test_sum_product.add(5, [3, 6, 9])

test_sum_product = [sum_product(num) for num in test_sum_product]
print(test_sum_product)
```