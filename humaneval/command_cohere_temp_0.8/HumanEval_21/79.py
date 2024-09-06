Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """
    min_value = min(numbers)
    max_value = max(numbers)
    return [((x - min_value) / (max_value - min_value)) for x in numbers]
```
The function `rescale_to_unit` works with a list of numbers, it first finds the minimum and maximum values in the list, and then calculates a linear transform to normalize the list. The transform is a linear interpolation between the smallest and the largest numbers in the list, thus making the smallest number become 0 and the largest number become 1.

To make sure the function behaves as expected we can write a couple of test cases:
```python
def test_rescale_to_unit():
    # Case with positive and negative numbers and one decimal
    assert rescale_to_unit([-2.0, -1.0, 0.0, 1.0, 2.0]) == [-0.0, -0.25, 0.0, 0.25, 1.0]

    # Case with small and large numbers (Ints and Doubles)
    assert rescale_to_unit([1, 2, 3, 4, 5]) == [0, 0.25, 0.5, 0.75, 1]

    # Case with only two elements
    assert rescale_to_unit([10, 5]) == [0, 0.5]

    # Case with equal elements
    assert rescale_to_unit([2, 2, 2, 2]) == [0, 0.25, 0.5, 0.75]
```