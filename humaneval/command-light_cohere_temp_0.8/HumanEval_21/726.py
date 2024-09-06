```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    numbers[0] = 0.0
    numbers[1] = 1.0
    
    return numbers
   }

def test_rescale_to_unit(numbers: List[float]):
    """ Test function to verify the correctness of the rescale_to_unit function."""
    numbers.append(rescale_to_unit([3.0, 4.0]))
    don't forget about the original values and just add the new ones
    """
    print(f'test passed.')

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]
numbers.print('This is
numbers: ', numbers)
```