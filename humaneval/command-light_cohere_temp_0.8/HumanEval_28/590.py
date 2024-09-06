```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string """
    return ''.join(strings)

# Test case 1: Empty list
assert concatenate([]):
   assert True

# Test case 2: Single string
assert concatenate('a'):
   assert 'a' == 'a'

# Test case 3: Two strings
assert concatenate(['a', 'b'])
   assert 'ab' == 'ab'

# Test case 4: Three strings
assert concatenate(['a', 'b', 'c'])
   assert 'abc' == 'abc'

# Test case 5: Mixed list
assert concatenate(['a', '1', '!2']) == '123'
``` 

This code defines a `concat` function that takes a list of strings as input and concatenates them into a single string. The `assert` statements are used to test the correctness of the `concat` function with various inputs. 

Remember to run this code using the Python interpreter or save it into a . file and run it using the .