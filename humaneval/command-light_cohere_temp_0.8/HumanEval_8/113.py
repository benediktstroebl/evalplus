```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, returns a tuple consisting of a sum and a product of all the integers in a list.
    Args:
        numbers (List[int]): A list of integers.
    Returns: a tuple (sum, product) where sum is the sum of the integers in the list, and product is the product of all the integers in the list.
    """

def test_sum_product() -> None:
    """
    Test the sum_product function by providing a sample list of integers.
    numbers = [range(5)]
    result = sum_product(numbers)
    assert result == (0, 1)
    assert sum(numbers) == 0
    assert product(numbers) == 1
    """
test_sum_product()
```