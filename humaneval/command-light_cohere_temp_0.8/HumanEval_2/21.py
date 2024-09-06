Here is a Python script that includes a self-contained function that solves the problem of truncating a number:
```python
import math
def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    return math.isfloor(number, 1e, 1)
```
This script defines a function, `truncate_number`, that takes a single argument, `number`. This function then uses the `math.hen` function `floor` to calculate the decimal part of the number, which is then returned.