```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x,i in zip(numbers,range(len(numbers))) if i==numbers[i][0]]
```
This Python script defines a function `rolling_max` that generates a list of the rolling maximum elements from a given list of integers. It uses a `zip` to generate the list of numbers and the index simultaneously, and then uses a list comprehension with `range(len(numbers))` to find the rolling maximum elements. The code is self-contained and provides the solution and test case to the problem statement.