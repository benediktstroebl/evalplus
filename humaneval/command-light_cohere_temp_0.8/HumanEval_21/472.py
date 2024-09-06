```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the input numbers
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This Python code defines a function called `rescale_to_unit`, which transforms a list of numbers into a new list such that the values are scaled to the range [0, 1] by dividing each number by 100. The code also uses the type hints for better code readability.