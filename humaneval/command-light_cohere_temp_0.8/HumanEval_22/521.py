```python
from typing import List
def filter_integers(values:
    # Filtering integers from the list
    return [num for num in values if type(num) == int]

# Testing the function
values_test = [1, 2, 3, 'abc', {}, [0]]
result = filter_integers(values_test)
print(result)  # Output: [1, 2, 3]
```