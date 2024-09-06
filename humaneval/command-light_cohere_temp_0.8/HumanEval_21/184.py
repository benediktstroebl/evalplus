Here's a solution to the problem:

```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    for num in numbers:
        if num < 0:
            return num * (-1)  # flip sign and rescale
        else:
            return num  # leave unchanged
    return numbers

def test_rescale_to_unit():
    input = [1.0, 2.0, 3.0, 4.0, 5]
   
    expected = [0.0, 0.0, 0.0, 0]
    return


test_rescale_to_unit() # Should print: [0.0, 0.0, 0]
```
Do you have any other Python-related questions or need further assistance with code?