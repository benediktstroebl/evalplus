```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```
This function takes a list of numbers and a threshold as inputs, it uses the `any` function with a lambda function to check for each pair of numbers in the list (`x, y`) if the difference between them is smaller than the threshold, if any of these comparisons is true, the function returns true, if none of them is true, it returns false. 

To test this function, you can use the following calls:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

This should return the same results as the example in the problem statement.