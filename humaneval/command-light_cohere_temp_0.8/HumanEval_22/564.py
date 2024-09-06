```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with various inputs
values_test = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
result_test = filter_integers(values_test)

print(result_test)  # Output: [1, 2, 3, 5]
``` 
This Python script defines a function called `filter_integers` that filters a list of values based on whether each element is an integer. It uses the simple for loop to iterate through the list and checks the `isinstance` of each element to an integer.