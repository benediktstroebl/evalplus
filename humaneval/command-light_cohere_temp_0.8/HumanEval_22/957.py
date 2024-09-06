```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', {}, []]
test_result = filter_integers(test_values)

print("Test case 1:", end="*value(test_result==[5]))
print("Test case 2:", end="*value(test_result==[['abc']]))
print("Test case 3:", end="*value(test_result==[]))
print("Test case 4:", end="*value(test_result==[1, 2, 3]))
``` 
The function `filter_integers` accepts a list of values and returns a new list with all the integer elements. 

The test cases validate the function's output by comparing it with the expected integer values.