```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Parameters: List[float] - A list of numbers.
    
    Returns: List[float] - A list of numbers with the smallest value set to 0 and the largest value set to 1.  """