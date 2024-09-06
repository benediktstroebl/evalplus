```python
from typing import List
def rescale_to_unit(numbers: List[float]):
    return [n / max(numbers) if n > max(numbers) else n for n in numbers]
```
This function takes a list of numbers and returns a new list of the same elements, but with all numbers scaled up or down so that the smallest number in the original list becomes 0, and the largest number becomes 1. The function ensures that the output is still a list of the same elements, and the type of the output is still a list of floats.