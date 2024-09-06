```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    :
        Apply the_rescale function

    Numbers are expected to be a list of at least two elements.

    Args:
        List[float] numbers: list of numbers to be scaled.

    Returns:
    List[float] scaled_numbers: list of rescaled numbers.
    """

Here is the test code:

def test_rescale():
    numbers = [1.0, 2.0, 3.0, 4.0]
   
    get_ numbers:
    print(rescale_to_unit(numbers))  # [0.0, 0.0, 0.0, 1.0] is the generate a output

test_rescale()

# 
The output should be the corresponding scaled numbers.