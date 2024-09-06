```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_results = [filter_integers(val) for val in test_values]

print("Test Cases:", test_values)
print("Expected Results:", test_results)

if all(test_results == [['a', 3, 5], [1, 2, 3], []]):
    print("Test cases passed.")
else:
    print("Test cases failed.")
```
The function `filter_integers` takes a list of values and returns a new list that contains only the integers from the input. It utilizes the filtration to filter out non-integer values.