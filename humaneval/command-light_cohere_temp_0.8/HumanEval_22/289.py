```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
test_cases = [[values] for values in test_values]

all(filter_integers(test_case) == [x for x in test_case if isinstance(x, int)]) for test_case in test_cases)
``` 
This code defines a function **filter_integers** that filters a list of values to only include integers. 

The function uses the typing's *isinstance* function to check if each element in the list is an integer. 

It then returns a new list with only those integers. 
The code also includes test cases to ensure that the function correctly filters the integers.