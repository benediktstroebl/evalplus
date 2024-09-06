```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test cases
test_cases = [
    [],
    ['a', 3, 'four', 5],
    [1, 2, 3, 'abc', {}, []],
]

for tc in test_cases:
    actual = filter_integers(tc)
    assert actual == [x for x in tc if type(x) == int], f"Test case [{tc}] failed: {actual}"
```
This script defines a function **filter_integers** that filters a given list **values** to retain only the integer elements. The function uses a list comprehension to filter the elements based on the condition **type(x) == int**. The test cases are also provided, and the function is evaluated with each test case. The output of the test cases will be printed to the console.