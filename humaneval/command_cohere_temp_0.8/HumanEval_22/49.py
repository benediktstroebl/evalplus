```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.

    :param values: List of any Python values.
    :return: List of integers contained in the input list.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers
```

The function employs a for loop to iterate through each value in the input list (`values`). For each value, it checks if the value is an instance of the `int` class using the `isinstance()` function. If true, it includes the value in the `integers` list, which it then returns. This approach allows the function to handle a variety of input types, such as strings, floats, dictionaries, and lists, without the risk of attempting unauthorized cast operations, as per the problem statement. 

This approach ensures that only valid integers are included in the resulting list while safely handling any non-integer values.