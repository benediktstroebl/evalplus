```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [x / (x + 1) for x in numbers]
    return numbers

# Test cases 

def test():
    assert rescale_to_unit([1.0, 2.0, 3.0, 4.0]) == [numbers([0.0, 0.0, 0]) # This test()

    assert rescale_to_unit([0.0, 0]) == [0.0] == [0]

    assert rescale_to_unit([0.0, 0.0]) == [([0.0, 0])]

    assert rescale_to_unit([0.0, 0, 0.0]) == [0.0, 0]

    assert rescale_to_unit([0.0, 0, 0, 0]) == [0.0] == [0]

    assert rescale_to_unit([0.75, 0.0, 0]) == [0.0, 0.75]

   73]

        assert rescale_to_unit([0.75, 0, 0, 0]) == [0.0, 0] == [0]

    assert rescale_to_unit([0.0, 0, 0, 0, 0]) == [0.0, 0] == [0]
```
The function `rescale_to_unit` takes a list of numbers and returns a new list with the same numbers, but each number has been rescaled. 
The test cases ensure that the function works as expected.