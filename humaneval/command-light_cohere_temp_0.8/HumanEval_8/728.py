```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args:
        numbers (List[int]): A list of integers
    Returns:
        Tuple[int, int]: A tuple with sum and product of the integers
    """
    return (sum(numbers), product(numbers))

# Unit tests
def test_sum_product():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3]) == (3, 3)
    assert sum_product([10, 20, 30]) == (60, 300)

# Usage
test_sum_product()
```