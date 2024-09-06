```python
from typing import List

def filter_integers(values: List[Any]) -> List[int]:
    result = [x for x in values if isinstance(x, int)]
    return result
```

The provided Python script defines a function called `filter_integers` that takes a list of values of any type specified in the type hint `List[Any]` and returns a list of integers. The function utilizes a list comprehension to iterate through each value in the input list, and checks if each value is an instance of the int class, which denotes an integer value. If it is an integer, it is included in the resultant list. The function then returns this filtered list of integers.

The function effectively removes non-integer values from the list, providing a streamlined list of integers. This is achieved without the need for additional import statements or nested functions, making the code concise and effective.

This solution can be directly invoked and tested for various input scenarios to verify its behavior and ensure its accuracy in filtering integers from a list of any values.