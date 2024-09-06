Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a transformed list such that the smallest number in the input list becomes 0, and the largest number becomes 1. This is achieved by calculating the smallest and the largest number in the input list, and then calculating the linear transform that achieves this goal and applies it to the elements of the list. 

To test this function, we can create a test that checks if the function correctly rescales the list [1.0, 2.0, 3.0, 4.0, 5.0]:
```python
def test_rescale_to_unit():
    # Act
    result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])

    # Assert
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert result == expected
```

This test verifies that the function `rescale_to_unit` when called with the input list `[1.0, 2.0, 3.0, 4.0, 5.0]` returns the expected output `[0.0, 0.25, 0.5, 0.75, 1.0]`.