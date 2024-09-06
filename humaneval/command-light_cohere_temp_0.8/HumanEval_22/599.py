```python
from typing import List
def filter_integers(values: 
    return [x for x in values if type(x) == int]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print(filter_integers(values1))  # [5]
print(filter_integers(values2))  # [1, 2, 3]
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses a list comprehension to filter out the integers.

The script also provides two test cases to verify the function.