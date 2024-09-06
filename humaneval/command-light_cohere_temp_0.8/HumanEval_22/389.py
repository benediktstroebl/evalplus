```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers only"""
    return [num for num in values if isinstance(num, int)]

# Test the function with a few inputs
values_test = [1, 2, 'three', 3.14, [1, 2, 3]]
result_test = filter_integers(values_test)
print(result_test)  # Output: [1, 2, 3]

# another test
values_another = [1, 2, 3, 'abc', {}, []]
result_another = filter_integers(values_another)
print(result_another)  # Output: [1, 2, 3]
```
This script defines a function called `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the input list. The function uses the particular type of each element in the input list to determine if it is an integer or not. 

The function is then tested with two different lists of values to ensure it is working correctly.