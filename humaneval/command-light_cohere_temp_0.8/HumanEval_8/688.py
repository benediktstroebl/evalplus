```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple containing sum and product of all integers in the list.
    """
    return (sum(numbers), sum(numbers) * product(numbers, numbers)))

def product(numbers: List[int]) -> List[int]:
    """
    Return the product of all the integers in the list.
    """
    return [**. list(map(lambda x: x, numbers)))

def sum(numbers: List[int]) -> int:
    """
    Return the sum of all the integers in the list.
    """
    return sum(numbers)

# Unit tests
test_sum_product = []
test_sum_product.append(
    [[]], 0)
test_sum_product.append(
    [ [1, 2, 3, 4], ()], (0, 24)
    )
test_sum_product.append(
    [1, 2], 1, 2, 3], (3, 6)
    )
test_sum_product.append(
    [4, 5, 6, 7], 1, 1
             10, 12, 15, 21)
test_sum_product.append(
    [2, 4, [1, 2], 3], (6, 24)
    )
test_sum_product.append(
    [(), [1, 2], [3, 4], 5], 0
    )

test_product = []
test_product.append(
    [[]], 1
)
test_product.append(
    [1, 2, 3], [4, 5, 6] ], 1, 120
    )
test_product.append(
    [1, 2, 3, 4, 5], [6, 7, 8, 9] ], 240
    )
test_product.append(
    [1, [10, 20, 30]], 1, 4160
    )
test_product.append(
    [10, 20, 30, 40], [1, 2, 3], 1], 4160
    )

def sum_product_test():
    """
    test_sum_product = test_product
    assert sum(test_sum_product) == (0, 1)
    assert sum(test_sum_product[0]) == 0
    assert sum(test_sum_product[1]) == 1
    assert sum(test_sum_product[2]) == 0
    assert sum(test_sum_product[3]) == 1
    assert sum(test_sum_product[4]) == 0
    assert sum(test_sum_product[5]) == 1
    assert sum(test_sum_product[6]) == 0
    assert sum(test_sum_product[7]) == 1
    assert sum(test_sum_product[8]) == 0
    assert sum(test_sum_product[9]) == 1
    assert sum(test_sum_product[10]) == 0
    assert sum(test_sum_product[11]) == 1
    assert sum(test_sum_product[12]) == 0
    assert sum(test_sum_product[13]) == 1
    assert sum(test_sum_product[14]) == 0
    assert sum(test_sum_product[15]) == 1
    assert sum(test_sum_product[16]) == 0
    assert sum(test_sum_product[17]) == 1
    assert sum(test_sum_product[18]) == 0
    assert sum(test_sum_product