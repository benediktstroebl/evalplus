```python
from typing import List
def filter_integers(values:
    filtered = [x for x in values if isinstance(x, int)]
    return filtered

# Test the function with markdown code block values
test_values = [['a', 3.14, 5], [1, 2, 3], ['abc', {}, []]

assert filter_integers(test_values) == [5, 1, 2, 3]
 ``` 
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses list comprehension to filter out the integers and returns the filtered list.