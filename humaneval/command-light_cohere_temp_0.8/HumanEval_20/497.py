```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]):
    # select the two closest elements and return them in order
    return (numbers[0] if numbers[0] < numbers[-1] else numbers[-1], numbers[0])
```
Do you need any assistance with other coding problems?