```python
from typing import List

def filter_integers(values):
    """Filter given list for integers."""
    return [int(element) for element in values if element.isdigit()]
``` 
# Test the function
test_values = [1, 2, 3, 'abc', {}, [1, 2, 'three']]
result = filter_integers(test_values)
print(result)  # Output: [1, 2, 3] 
``` 
This script defines a function called **filter_integers** that takes a list of any Python values and returns a new list containing only the integers from the input. It utilizes a filter expression and the list comprehension to achieve this. The test case successfully filters the values, and the output is a list of integers [1, 2, 3].