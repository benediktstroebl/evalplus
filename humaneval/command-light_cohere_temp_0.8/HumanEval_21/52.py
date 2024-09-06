Here is a self-contained Python script that solves the problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers


# Testing the function with sample inputs
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = [0.0, 0.0, 0.0, 0.0]
# Testing the input and expected output using markdown code block.