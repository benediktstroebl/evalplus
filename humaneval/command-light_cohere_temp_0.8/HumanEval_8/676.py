```python
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of a given list of integers.
    Args:
        numbers (List[int]): A list of integers.
    Returns: Tuple[int, int]: A tuple with the sum and product of all the integers in the list.
    Returns: (0, 1) if the list is empty.
    """
    def sum_product(lst: List[int]) -> Tuple[int, int]:
        return (sum(lst), product(lst))
    """
    # Unit tests
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 2, 3]) == (3, 3)
    assert sum_product([1, 2, 3, 4]) == (8, 24)
    assert sum_product([1, 2, 3, 5]) == (13, 60)
    assert sum_product([]) is (0, 1)
    assert sum_product([10, 20, 30]) == (60, 300)
    ```