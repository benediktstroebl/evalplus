```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [(x-min(numbers))/(max(numbers)-min(numbers))*1 for x in numbers]
```

The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers rescaled to the range between 0 and 1 (inclusive). The transformation is a linear transformation that makes the smallest list element 0 and the largest list element 1.

This implementation ensures that the returned list always has the same length as the input list, and the elements in the returned list are proportional to the elements in the input list, with the smallest and largest values scaled to 0 and 1, respectively. 

The `typing` module is used to declare the input parameter as a list of floats. This declaration helps ensure that the function is called with the correct input type and provides better code readability. 

This solution can be tested by calling the function with a list of test cases, such as `[1.0, 2.0, 3.0, 4.0, 5.0]`. The expected output is `[0.0, 0.25, 0.5, 0.75, 1.0]`.