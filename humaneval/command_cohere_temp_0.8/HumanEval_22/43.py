```python
from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    integers = []
    for value in values:
        if isinstance(value, int):
            integers.append(value)
    return integers

# Tests
values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # Expected output: [1, 2, 3]
``` 

The `filter_integers` function takes a list of values of any type and returns a list of integers. It achieves this by iterating through each value in the input list. If the current value is an integer, it is added to the integers list, which is returned at the end. The test case demonstrates the usage of the function and prints the expected output `[1, 2, 3]`. 

If you would like to see more details about the problem or the solution, let me know.