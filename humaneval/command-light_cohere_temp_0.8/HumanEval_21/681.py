```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    numbers = [x / 100 for x in numbers[::-1]: x = max(0, x) / 100 return numbers

# Test cases
test_cases = [
    [0.0, 0.0, 0.0, 0.0, -.2, 4.0, 0.0],
   1,  [100.0, 200.0], [0.01, 0.0, 10.0, 1.0], [0.1, 0.0], [0.5, 0.0, 2.0, 0.5, 0.2, 2, 0, 0.0, 100.0]

test_cases)

test_cases = [rescale_to_unit(test_cases) if isinstance(test_cases, List)] else test_cases
```
This script defines a function `rescale_to_unit` that scales a list of numbers to the range [0,1]. It also includes a few test cases to test the function. The function uses the range [0,100] to scale the numbers and then returns the scaled numbers.