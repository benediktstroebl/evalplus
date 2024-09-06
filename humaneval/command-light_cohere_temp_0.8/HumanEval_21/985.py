```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers.extend(1.0, 2.0, 3.0, 4.0, 5)
   0, 0.0, 0)
    0.0, 0.0)
   0.0, 0)
   
0.0, 1) # and [::-1] in descending order)"""

def test_rescale_to_unit(numbers: List[float]):
    return all([numbers[i] >= 0 and numbers[i] <= 1 for i in range(len(numbers))])

# Example
numbers = [1.0, 2.0, 3.0, 4.0, 5]

print(test_rescale_to_unit(numbers))  # True
```