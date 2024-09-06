Here is a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    numbers.res[0] = 0
    numbers[1:] = 1
    return numbers
```

This function takes a list of numbers as input and returns a list of the same numbers with the first element set to 0 and the second element set to 1.