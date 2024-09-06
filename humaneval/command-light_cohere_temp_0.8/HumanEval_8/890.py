```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ 
    Calculate the sum and product of a list of integers.
    Args:
    numbers: A list of integers.
    Returns: A tuple of sum and product of the numbers.
    """

>>> sum_product([1, 2, 3, 4]) == (10, 24)
"""

def test_sum_product():
    return sum_product([1, 2, 3, 4]) == (10, 24)

# Driver code
if __name__ == "__main__":
    print("Testing function...")
    assert test_sum_product()
    print("Tests passed!")
```