Here is a Python script that contains a self-contained function that solves the problem of rescaling a list of numbers to the unit range of [0,1]:

```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the rescaling transformation
    numbers_rescaled = [num / max(numbers) for num in numbers]
    # Return the rescaled numbers
    return numbers_rescaled

def test_rescale_to_unit():
    # Test the function
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   2
   5.

    # Call the0
    test_rescale_to_unit(numbers)
    assert numbers == [0.0, 0.0, 0.0, 0.0]
```
The above code defines the `rescale_to_unit` function, which takes a list of numbers as an argument and returns a new list of the same numbers after applying a linear transformation.

The test_rescale_to_unit function is a simple unit test that passes the `rescale_to_unit` function to a list of numbers and checks that the resulting list is equal to `[0,0,1,10]`.