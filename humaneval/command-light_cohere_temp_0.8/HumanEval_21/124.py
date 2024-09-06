```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    If there is at least two elements, the function will return a list of numbers where the first element is the original number, and the remaining are the transformed numbers.
    
    Numbers are expected to be positive numbers.
    """ The
    expected return type: List[float]
    """
    numbers[0] = 0
    numbers = [numbers[0]] + [x * numbers[0] for x in numbers[1:]]
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5]
numbers = rescale_to_unit(numbers)

print(numbers)
```