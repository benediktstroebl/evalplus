```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function
test_values = [1, 2, 3, 'abc', [1, 2], {}]
result = filter_integers(test_values)
print(result)  # Output: [1, 2, 3]
```
The function `filter_integers` takes a list of values and returns a new list containing only the integers from the input. The function uses a list comprehension to iterate over the values and filter out the integers.