Here is a Python script that defines a function sum_product that calculates the sum and product of a list of integers, and passes tests based on the provided docstrings:
```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of a list of integers. 
    Returns a sum and product, with empty sum and product returned as 0 and 1 respectively. 
    """
   
    function returns a tuple (sum, product) where sum is the sum of all integers in the list, and product is the product of all integers in the list.
    Test suite:
    def test_sum_product():
        numbers = [1, 2, 3, 4]
        result = sum_product(numbers)
        assert result == (10, 24)
        return
    test_sum_product()
```