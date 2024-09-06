Here is a Python script that contains a self-contained function to solve the problem and pass the test:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    return [x * 1.0 for x in numbers] if all(x > 0) else numbers

# Test case:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 0.0])  #