```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    result: List[int] = []
    for value in values:
        if isinstance(value, int):
            result.append(value)
    return result

# Tests
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Expected output: [1, 2, 3]
``` 

The function `filter_integers` takes a list of values of any type and returns a list of integers by filtering out all elements that are not integers. The resulting list only contains integers that are present in the initial list. 

To achieve this, the function utilizes Python's `typing` module to declare the input parameter as a list of any type (`List[Any]`). This allows the function to handle a variety of input types. The function then uses a typed variable `result` to store the filtered integers, ensuring that only integers are added to the output list. 

The example usage and test case demonstrate the function's behavior, filtering out non-integer elements from the input list, and returning only the integers.[1] 

1. Note that the function assumes that the input list contains only valid Python values (e.g., integers, strings, dictionaries, or lists). If the input list contains invalid or complex types, the function may not handle them correctly.