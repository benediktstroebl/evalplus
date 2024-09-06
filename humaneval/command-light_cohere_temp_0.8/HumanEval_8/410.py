```python
from typing import List

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Calculate the sum and product of all integers in a list.
    Args: numbers (List[int]): A list of integers.
    Returns: Tuple[int, int]: A tuple with a sum and a product of all integers.
    Return value iss (0, 1) if the list is empty.
    """

def test_sum_product() -> None:
    """
    Test the function by providing a sample list of integers.
    Args: numbers (List[int]): A list of integers.
    """
    test that the list is empty, the function returns (0, 1).
    """
    return_values = sum_product([0, 1])
    assert return_values == (0, 1)
    
    # Test with another list of integers.
    return_values = sum_product([1, 2, 3, 4])
    assert return_values == (10, 24)
```