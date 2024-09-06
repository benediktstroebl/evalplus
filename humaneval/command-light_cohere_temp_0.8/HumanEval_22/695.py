```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function
values_list = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values_list)
print(result)  # Output: [1, 2, 3]

values_list_optional = [1, 2, 3, 'abc', None, [], ]
result_optional = filter_integers(values_list_optional)
print(result_optional)  # Output: ['1', '2', '3']

values_list_error = ['a', 3.14, (1)]
with pytest.org.assert.check.raises(ValueError('Input expected ain a list of objects'))
```