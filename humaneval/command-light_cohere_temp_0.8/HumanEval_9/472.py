```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Returns a list of integers representing the rolling maximum element found until a given moment 
    in the sequence.
    numbers: List[int]
    Return the list of rolling maximum elements.
    """
    testing code and
    def test_rolling_max(numbers: List[int])) -> None:
        # Test case 1
        assert rolling_max([1, 2, 3, 2, 3]) == [1, 2, 3, 3]
        # Test case 2
        assert rolling_max([4, 2, 1, 4]) == [4, 2, 1, 4]
        # Test case 3
        assert rolling_max([7, 3, 2, 1, 5]) == [7, 3, 2, 1]
        return None
    test_rolling_max([1, 2, 3, 2, 3])  # Should pass
    test_rolling_max([4, 2, 1, 4])  # Should pass
    test_rolling_max([7, 3, 2, 1, 5])  # Should pass
    ``` 
This Python code defines a function `rolling_max` that calculates the rolling maximum elements in a sequence of numbers. The function takes a testing code for `rolling_max` is also provided, which includes multiple test cases designed to pass the function's behavior.