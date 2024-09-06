```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input:
    numbers: List[float] - list of numbers to be scaled.

    Output:
    rescaled_numbers: List[float] - list of scaled numbers.

Test case 1:
In the given list [1.0, 2.0, 3.0, 4.0, 5], the is the input for the rescale_to_unit function, and the output is: [0.0, 0.0, 0.0, 0.0, 0.0] 

numbers: [1.0, 0.0, 0.0, 0.0, 0.0]