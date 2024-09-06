Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    return [num / min(numbers) for num in numbers] if len(numbers) > 1 else numbers[0]

test_input = [1.0, 2.0, 3.0, 4.0, 0.0, 0.0]

assert rescale_to_unit(test_input) == [0.0, 0.0, 0.0, 1.0]
```