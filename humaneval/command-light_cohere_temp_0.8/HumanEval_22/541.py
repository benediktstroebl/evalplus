```python
from typing import List
def filter_integers(values:
    in_ints = [x for x in values if type(x) == int]
    return in_ints

# Test the function with markdown code block
# Each element should be an integer
test_values = [1, 2, 3, 'abc', {}, [5, 6], [7, 8, 9] ]
print(filter_integers(test_values))  # Output: [1, 2, 3, 5, 6]
``` 
This function uses a generator expression to filter out any values that are not integers, and then returns a list of the remaining integers.