Here's the self-contained Python script that solves the problem you described: 

```python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    :type numbers List[float]
    :type threshold float
    return any(map(lambda x,y: abs(x-y)<threshold,numbers))
```

The script defines a function called `has_close_elements` that takes two arguments: a list of numbers (`numbers`) and a threshold value (`threshold`). The function returns `True` if there are any two numbers in the `numbers` list that are closer than the `threshold`, and returns `False` otherwise. 
This is achieved using the map function, which applies a lambda function to each pair of numbers in the list. The lambda function checks if the absolute difference between two numbers is less than or equal to the `threshold`.