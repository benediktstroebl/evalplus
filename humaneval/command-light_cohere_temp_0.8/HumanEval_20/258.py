```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # input validation
    assert len(numbers) == 2, "Error: Input list must contain exactly two numbers."
    # compare elements
    a, b = numbers[0] - numbers[1], numbers[1] - numbers[0]
    # return first closest number, in case of tie
    return (a, b)
```