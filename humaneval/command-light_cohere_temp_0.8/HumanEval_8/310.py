```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all the integers in a list.
    Args: numbers (List[int]): A list of integers.
    Returns: (int, int): A tuple with sum and product of all integers.
    """
    test_sum_product([]) = (0,1)
    """
    return (sum(numbers), product(numbers))

# Test suite
def test_sum_product():
    test_list = [1,2,3,4]
    result = sum_product(test_list)
    assert result == (4, 12)
```