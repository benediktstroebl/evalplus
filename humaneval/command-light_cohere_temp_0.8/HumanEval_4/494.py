```python
from typing import List

def mean_absolute_deviation(numbers):
    return math.abs((sum(numbers) / len(numbers)) - numbers[-1])

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 0.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) == 0.0
```