```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Input validation
    assert len(numbers) > 1, "Error: Input list must contain at least two elements"
    # Transform
    return [0.0 if n < 0 else 1.0 if n == 1 else n for n in numbers]

# Example of usage
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 5.0]
return rescale_to_unit(numbers)
```