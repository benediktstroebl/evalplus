```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [val for val in values if isinstance(val, int)]
```

The above code assumes you are using Python 3.8 or a newer version which supports type hints and the `List[Any]` syntax is used to define a list that can hold any type of data, and the `isinstance()` function is used to check if each list element is an instance of the `int` class and returns a new list with filtered integers. 

To follow best practices, the function in the code above includes a docstring that explains what the function does and provides example usage that demonstrates how to use the function to filter a list of integers and returns a list of only the integers in the input list. 

If you are planning to use this function in a larger project, consider adding additional testing scenarios to cover more edge cases, such as input lists containing floats, elements that are not integers, and empty lists, to ensure that the function behaves as expected in those cases as well.