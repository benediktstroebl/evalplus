Here is a self-contained Python script that solves the markdown code block:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[0] = 0
    for i in range(1, len(numbers)):
        numbers[i] = (numbers[i] - numbers[i-1]) / (numbers[i-1] - numbers[i-0])
    return numbers
```
The function takes a list of numbers as input and applies a linear transformation to the list to ensure that the smallest number in the list becomes 0. The function then returns the for a list of numbers, with each number scaled to a unit.