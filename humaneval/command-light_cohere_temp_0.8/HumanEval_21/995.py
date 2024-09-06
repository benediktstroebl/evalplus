Here is a self-contained Python script with a function that solves the problem you've described:

```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Apply a linear transform to the list of numbers
    numbers = [x / 100.0 for x in numbers]
    return numbers


# Test case:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
result = [0.0, 0.0, 0.0, 0.0]

# Test case:
pass
``` 
Please note that you can use this function to transform any list of numbers in your markdown code.