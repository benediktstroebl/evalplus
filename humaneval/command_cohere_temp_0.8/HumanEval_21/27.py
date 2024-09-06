Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    return [((x - min(numbers)) / (max(numbers) - min(numbers))) for x in numbers]
```
The function `rescale_to_unit` takes a list of numbers as input and returns a list of numbers scaled to the range [0, 1] based on the smallest and largest values in the input list. This approach uses Python's list comprehension and arithmetic operations to perform the rescaling. It is easier to understand and more straightforward than using `map` or `apply` functions with a lambda function, especially for this particular problem. Also, there is no need for a return statement with a `None` value. 
This function can be tested by calling it with a list of values, such as `[1.0, 2.0, 3.0, 4.0, 5.0]`, and verifying that the output is `[0.0, 0.25, 0.5, 0.75, 1.0]`.