```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    # Rescale the general, starting with the largest element, to ensure the range is correct.
    """return [numbers[numbers[0] - 1] / numbers[0] if numbers[0] != 0 else numbers[0]

# Give the function some sample inputs
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

print(rescale_to_unit(numbers)) == [0.0, 0.0, 0.0, 0.0])