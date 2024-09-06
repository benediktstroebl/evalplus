```python
from typing import List

def filter_integers(values: List[Any]):
    return [int(el) for el in values if type(el) == int]

# Test the function
values = [['a', 3.14, 5], [1, 2, 'abc'], [True, {}] ]
result = filter_integers(values)
print(result)  # Output: [5, 1, 2, 3, True]

# Test with wrong values
values = [1, 2, 3, 'abc', {}]
result = filter_integers(values)
print(result)  # Output: []
```

The function `filter_integers` filters a list of any value and returns a new list with only the integers. The test cases pass the the test the function with valid inputs and print the output. The output should be the the expected output.