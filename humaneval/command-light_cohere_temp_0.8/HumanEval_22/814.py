```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3

# Test case 2
test_values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(test_values)
assert len(result) == 3

# Test case 3
test_values = List(range(1, 1000))
result = filter_integers(test_values)
assert len(result) == 500
```
The provided Python code defines a function `filter_integers` that filters a list of any values based on the condition that their type is `int`. The function uses the `type()` built-in function to check the type of each element in the input list. The code is then creating three different test cases to validate the correctness of the `filter_integers` function.