Here's the provided Python script with the self-contained function:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / 100.0 for x in numbers]
    return numbers
```
Do you need any further assistance with the code?