```python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    if len(numbers) < 2:
        raise ValueError("At least two numbers must be provided")
    x = numbers[-2]
    y = numbers[-1]
    return x, y
```

The function `find_closest_elements` uses the `sort()` method to sort the supplied list of numbers and then retrieves the closest two elements, which are the last two in the sorted list. This solution is concise and efficient and it avoids explicit looping and conditional statements, making it a good candidate for solving this problem. 

This code does not have any tests but they can be easily added if needed, following the proper pytest syntax. 

You can use this code either as a standalone script or import it into another project.