```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not of type `int`. It uses a list comprehension that iterates over each value in the input list and adds an integer value to the `integers` list if the current value is an integer. And this way, the function creates a new list that contains only the integer values from the original input list. 

Here is an example of how you can use the function to test it:
```python
filter_integers(['a', 3.14, 5])
```
```
[5]
```

And here is another example:
```python
filter_integers([1, 2, 3, 'abc', {}, []])
```
```
[1, 2, 3]
``` 

This shows how the function only returns the integer values from the input lists, removing all other values.