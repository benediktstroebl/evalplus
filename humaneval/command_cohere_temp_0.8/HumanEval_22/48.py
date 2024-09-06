```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_list = [item for item in values if isinstance(item, int)]
    return int_list
```

The above code assumes the presence of a predefined function `isinstance` which returns `True` if the input argument is an instance of the type mentioned as the second argument and `False` otherwise. 

The function `filter_integers` accepts a list of values and returns a list of filtered integers. It uses a list comprehension that iterates through each value in the provided list of arbitrary values. For each value, it uses the `isinstance` function to check if the value is an instance of the integer type, and if so, includes it in the new list. The resulting list of integers is then returned as the output. 

The function docstring provides helpful examples that explain its usage and expected behavior. 

```python
filter_integers(['a', 3.14, 5])
```
```
[5]
```

```python
filter_integers([1, 2, 3, 'abc', {}, []])
```
```
[1, 2, 3]
``` 

You can also use the `type` function to directly compare the type of each value in the list:
```python
def filter_integers(values: List[Any]) -> List[int]:
    int_list = [item for item in values if type(item) == int]
    return int_list
``` 

Which produces the same result. 

This method is less efficient because it checks the type each time, while `isinstance` checks the type definition only once, caching the result for future comparisons.