```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function
test_values = [1, 2, 3, 'abc', {}, [0]]
test_output = filter_integers(test_values)
print(test_output)
``` 
This function, `filter_integers`, filters a list of values for only integers. The function uses the filter() function along with the isinstance() built-in function to check if each element in the list is an instance of an integer. The function returns a filtered list of integers. 

Please note that the function is self-contained and has no external dependencies.