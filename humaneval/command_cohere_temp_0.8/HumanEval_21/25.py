Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_value = min(numbers)
    max_value = max(numbers)
    scaled_numbers = [((x - min_value) / (max_value - min_value)) * 255 for x in numbers]
    return scaled_numbers
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1]. The function works by first finding the minimum and maximum values in the input list using the `min` and `max` functions. Then, a list comprehension applies the linear scaling transformation to each number in the list.

The script can be tested by calling the function with a list of values, such as `[1.0, 2.0, 3.0, 4.0, 5.0]`. The expected output is `[0.0, 0.25, 0.5, 0.75, 1.0]`. 

Here is a test suite to verify the functionality of the script:
```python
def test_rescale_to_unit():
    # Test single list
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    expected = [0.0, 0.25, 0.5, 0.75, 1.0]
    assert rescale_to_unit(numbers) == expected

    # Test multiple lists
    numbers = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
    expected = [[0.0, 0.5, 0.75], [0.5, 0.625, 0.75], [0.75, 0.83333, 1.0]]
    assert rescale_to_unit(numbers) == expected

    # Test single value
    assert rescale_to_unit(5.0) == [0.5]

    # Test empty list
    assert rescale_to_unit([]) == []

    # Test single element list
    assert rescale_to_unit([3.0]) == [0.5]

test_rescale_to_unit()
```

The test suite includes multiple scenarios that the `rescale_to_unit` function should handle correctly.