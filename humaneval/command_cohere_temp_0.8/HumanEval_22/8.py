```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    return [x for x in values if isinstance(x, int)]
```

The above code assumes the given test cases in the problem description, where:
- The `values` variable is a list of arbitrary Python values.
- The goal is to return a new list that contains only the integer values from the original list.

The function achieves this using a list comprehension together with the `isinstance()` function to filter out values that are not instances of the `int` class, producing a new list that contains only the integers from the input list. 

Overall, the code adheres to the specified problem description and provides an efficient and concise solution.  It can be verified using the following tests:
```python
filter_integers(['a', 3.14, 5]) # [5]
filter_integers([1, 2, 3, 'abc', {}, []]) # [1, 2, 3]
``` 
This is because the first test case contains a list of values ['a', 3.14, 5], and the second case contains a list [1, 2, 3, 'abc', {}, []]. After filtering, the first result is [5], and the second results in [1, 2, 3], which are the expected outputs.