```python
from typing import List, Optional

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers: List[int] = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Expected output: [1, 2, 3]
``` 

The function `filter_integers` works by using a list comprehension to filter out any elements that are not instances of int and then appending only the integer values to the `integers` list. 

To follow best practices, the function includes type annotations, which help provide useful documentation and make the code more robust. These annotations specify that the function takes a list of any type (`List[Any]`), but returns a list of integers (`List[int]`). 

The behavior of the function is illustrated through tests. In the test case `values = [1, 2, 3, 'abc', {}, []]`, the function is expected to return `[1, 2, 3]`, as it should filter out non-integer values. 

To run the tests, you can modify the script and add the test cases (e.g., add more test cases to the `values` list and adjust the expected outputs accordingly).