```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter a given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: A list of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

This function uses a list comprehension to create an integer list called `integers`, which collects integers from the input list. Finally, the function returns the `integers` list, which contains only the integers from the input list. 

Here is an example of how you can use the function to test its functionality:
```python
filter_integers(['a', 3.14, 5]) == [5]
filter_integers([1, 2, 3, 'abc', {}, []]) == [1, 2, 3]
``` 
The example usage demonstrates the expected output of the function when used with different input lists.