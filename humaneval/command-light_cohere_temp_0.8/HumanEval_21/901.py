```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation
    numbers_res = [x / (x <= 0.0) for x in numbers]
    return numbers_res

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 1.0])
```