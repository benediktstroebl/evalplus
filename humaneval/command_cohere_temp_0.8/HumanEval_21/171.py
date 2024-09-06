```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    """
    return [(x-min(numbers))/(max(numbers)-min(numbers)) for x in numbers]
```

The function `rescale_to_unit` calculates the minimum and maximum values in the input list and then divides each element in the list by the difference between the maximum and minimum values. This transform scales the values so that the smallest number becomes 0 and the largest number becomes 1. The resulting list of transformed values is then returned.  The expected behavior is encapsulated in the following test:
```python
def test_rescale_to_unit():
    # Arrange
    input_list = [1.0, 2.0, 3.0, 4.0, 5.0]

    # Act
    scaled_list = rescale_to_unit(input_list)

    # Assert
    assert scaled_list == [0.0, 0.25, 0.5, 0.75, 1.0], "Failed to rescale the list correctly."
```

This test case verifies that the function `rescale_to_unit` transforms the provided input list correctly. Specifically, it checks whether the rescaled list matches the expected output, thus covering the functionality of the function.