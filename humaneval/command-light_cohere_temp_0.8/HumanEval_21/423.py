```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply linear transformation to the input numbers to map them to the range [0, 1]
    numbers_transformed = [x / 100.0 for x in numbers]
    return numbers_transformed
```