Here's the solution:
```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [num / min(numbers) for num in numbers] if len(numbers) > 1 else numbers]
```
Do you require assistance with any other Python tasks or code solutions?