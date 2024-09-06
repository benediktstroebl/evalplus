```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    # Conversion to ensure all numbers are between 0 and 1
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 5.0]
print(rescale_to_unit(numbers)) == [0.0, 0.0, 0.0, 0.0, 1.0])
```