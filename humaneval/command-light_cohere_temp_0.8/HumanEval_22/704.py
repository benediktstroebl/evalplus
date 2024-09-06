Here is a self-contained Python script that solves the problem of filtering integers from a given list of any Python values:
```python
from typing import List

def filter_integers(values:
    # Filter the given list for integers
    integers = [x for x in values if type(x) == int]
    return integers

# Test the function with sample inputs
values_list = [1, 2, 3, 'abc', {}, [5], [3.14] ]
 print(filter_integers(values_list))
``` 
This function takes a list of values and returns a new list containing only the integers from the original list. The test cases have been provided to demonstrate the functionality of the function.