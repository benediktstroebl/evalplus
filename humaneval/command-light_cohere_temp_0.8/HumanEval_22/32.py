```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Example values
values_list = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]

print(filter_integers(values_list))  # Output: [5, 1, 2, 3]
``` 
This script provides a function, `filter_integers`, that takes a list of values and returns a new list containing only the integers from the input. The function uses a filtering logic within the function body to accomplish this. The example values are passed to the function and the output is displayed.