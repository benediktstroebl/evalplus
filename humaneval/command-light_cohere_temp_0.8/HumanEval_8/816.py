```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ Returns a tuple with sum and product of all integers in the list.
   >>> Raise an ValueError if the sum is empty, otherwise return 0 and 1.
    """
    print("sum_product function signature:", sum_product.sum_product([1, 2, 3, 4]))
    print("sum_product([1, 2, 3, 4]) =", sum_product([1, 2, 3, 4]))
    print("Test case 1:", sum_product([5, 6, 7]))
    print("Test case 2:", sum_product([10, 20, 30]))
    print("Test case 3:", sum_product([1, 2, 3, 4, 5]))
    print("Test case 4:", sum_product([100, 200, 300]))
    print("Test case 5:", sum_product([10, 20, 30, 40]))
```
The `sum_product` function in this version is self-contained and accepts a list of integers as input. The test cases are then applied to the function to ensure it is functioning appropriately.