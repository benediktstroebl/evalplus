```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This transformation is a linear transformation often used in data normalization.

This script includes type annotations provided as `List[float]` to ensure the function accepts a list of floats and returns a list of floats too. 

To ensure this function behaves as expected, it is recommended to write tests targeting different scenarios. Below is an example of such tests:
```python
def test_rescale_to_unit():
    # Test list with single element
    scaled = rescale_to_unit([10.0])
    assert scaled == [0.0]

    # Test list with two elements
    scaled = rescale_to_unit([5.0, 10.0])
    assert scaled == [0.25, 0.5]

    # Test list with three elements
    scaled = rescale_to_unit([1.0, 2.0, 3.0])
    assert scaled == [0.0, 0.5, 1.0]

    # Test list with multiple elements
    scaled = rescale_to_unit([0.5, 1.0, 2.0, 3.0, 4.0])
    assert scaled == [0.25, 0.5, 0.75, 1.0, 1.0]

```

These tests check if the function handles different-sized input lists, including edge cases like an empty list ([]) or a list with a single element [10.0]. Each expected output is a list with the same number of elements as the input list, rescaled to fit the range [0, 1].  Other tests could potentially check for errors like having less than two elements in the list or checking if the function works properly with negatives or other edge numbers.