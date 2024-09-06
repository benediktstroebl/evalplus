```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generates a list of rolling maximum elements from a given list of integers.
    Each element in the maxes is computed by repeatedly taking the maximum of the current element and the next element,
    until the current element becomes smaller than the next.
    Args:
        List[numbers] - list of integers.
    Returns: list of integers which the rolling maximum elements are generated.
    """


test_rolling_max = []
def test_rolling_max(test_set: List[int]) -> None:
    test_rolling_max.append(rolling_max(test_set))
# Example usage:
numbers = [1, 2, 3, 2, 3, 4, 2]
test_set = [1, 2, 3, 4, 5]
test_rolling_max(numbers)
test_rolling_max(test_set)
 ```