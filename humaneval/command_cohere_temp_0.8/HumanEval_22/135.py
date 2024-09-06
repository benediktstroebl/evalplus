```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The above code provides an implementation of the filtering function `filter_integers`, which takes a list of values of any type and returns a list of integers. The function utilizes Python's list comprehension to iterate through each value in the input list. For each value, it checks if the value is an instance of the `int` class using the `isinstance()` function. If it is, the value is included in the resultant list. Finally, the function returns the list of integers. 

To perform unit testing, you can use the `assert` statement in Python to check whether the output of the function is as expected for a given input. Here is an example:
```python
assert filter_integers(['a', 3.14, 5]) == [5]
assert filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
```

In the above tests, the `assert` statement checks whether the filtered list of integers matches the expected output for two different inputs. If the values are truthy, the tests pass; otherwise, they fail.  This allows you to validate the correctness of the function implementation.