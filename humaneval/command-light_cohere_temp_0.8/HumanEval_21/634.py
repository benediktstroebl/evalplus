```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply linear transformation to numbers
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers)) == [0.0, 0.0, 0.0, 0.0])
```