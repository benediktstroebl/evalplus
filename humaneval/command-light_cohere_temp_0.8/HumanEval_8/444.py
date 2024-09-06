```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple consisting of a sum and a product of all the integers in the list """
    product = 1
    sum = 0 
    for num in numbers:
        product *= num
        sum += num
    return (sum, product)

#unit tests
test_sum_product = [
    ( [], 0),
    ( [1], 1),
    ( [1, 2], 2),
    ( [1, 2, 3], 6),
    ( [1, 2, 3, 4], 24),
    # empty list test
    ( [], 1 )
]

for test in test_sum_product:
    actual = sum_product(test)
    expected = test
    print(f"Test case {test} failed: {actual}, expected)")
```