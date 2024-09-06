```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    The rescale_to_unit function takes a list of numbers and returns a new list of numbers, where each number in the original list has been transformed by a linear transformation. The linear transformation is such, defined by the function, maps the number 0 to 0 and the number 1 to 1.

    For example, if the input list is [1.0, 2.0, 3.0, 4.0, 0], then then be transformed to [0.0, 0.0, 0.75, 1.0], respectively. This transformation guarantees that numbers in the list are scaled to the range [0, 1] as desired.

    Test case for the0.0, the input list will a list of numbers, and the function will return the corresponding transformed list.

```