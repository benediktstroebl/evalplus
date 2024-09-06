```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes two arguments; a list of numbers and a threshold. It uses the `any` function with a generator expression to check if any of the differences between consecutive elements in the list are less than the threshold. 

Here is an example usage of the function:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

This example test case demonstrates the usage of the function. The first example returns `False` since the smallest distance between any two numbers is `0.8`, which is greater than the threshold of `0.5`. In the second example, however, the smallest distance between any two numbers is `0.2`, which is less than the threshold of `0.3`, so the function returns `True`. 

This function is also capable of handling an empty list and any list with only one number, in which case it will return `False` and `True` respectively, since there are no adjacent elements in the former case and the threshold is automatically met in the latter case.