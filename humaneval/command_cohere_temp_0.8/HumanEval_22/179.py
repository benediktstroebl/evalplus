```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result = [x for x in values if isinstance(x, int)]
    return result
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not instances of the integer class `int` using a list comprehension and the `isinstance` function. As the function result is neither a string, nor an integer, nor a float, nor a boolean, nor a tuple, nor a list, nor a dictionary, nor a set, nor an object, nor an enum, nor a dataclass, the type annotation of the return type is set to `List[int]`. 

Here is an example of using the `filter_integers` function:
```python
filter_integers(['a', 3.14, 5])
```
```
[5]
```

And here is another example of using the `filter_integers` function:
```python
filter_integers([1, 2, 3, 'abc', {}, []])
```
```
[1, 2, 3]
``` 

In both cases, the function is filtering out all elements that are not integers, and returning a list of integers.