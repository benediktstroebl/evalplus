```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculates the sum and product of a list of integers.
    Args: 
        numbers: list of integers
    Returns:
        A tuple containing the sum and product of the given list.
    """

def test_sum_product() -> None:
    """
    Test function to validate the sum_product function.
    Args:
        numbers: list of integers
    Returns:
    None
    """
    numbers = [1, 2, 3, 4]
    result = sum_product(numbers)
    print(f"sum: {result[0]}, product: {result[1]}")
    assert result == (10, 24)
```