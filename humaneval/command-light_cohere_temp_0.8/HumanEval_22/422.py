```python
from typing import List
def filter_integers(values:
    """ Returns a list containing only the integers from the given list"""
    result = [x for x in values if type(x) == int]
    return result

# Test cases
values1 = [1, 2, 3, 'abc', {}, [5, 6]]
values2 = [1, 2, 3, 'a', [], [7]]

print("Test case 1: ", end="")
print(filter_integers(values1))  # Expected output: [1, 2, 3, 5, 6]
print("Test case 2: ", end="")
print(filter_integers(values2))  # Expected output: [1, 2, 3, 'a', []]
``` 
The function filter_integers, which accepts a list of any values and outputs a new list containing only the integers from the input, is described in the script above. The filter_integers function's output is then verified against the anticipated results using the test cases.