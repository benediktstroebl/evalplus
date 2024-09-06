```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the `List[Any]` type hint. The function filters this list to include only the elements that are instances of the `int` type, and returns the resulting list of integers. It utilizes Python's list comprehension, along with the `isinstance()` function, to achieve this filtering mechanism. 

This function is a straightforward solution for the provided problem, effectively demonstrating how to filter a list of heterogeneous values to include only the integers, as demonstrated by the test cases provided earlier. 

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