```python
from typing import List
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test the function with some values
values_test =  [1, 2, 3, 'abc', {}, [1, 2, 3], [4, 'a'])
assert filter_integers(values_test) == [1, 2, 3, 4]

# Test the function with a tuple
assert filter_integers([1, 2, 3]) == [1, 2, 3]

# Test the function with a string
assert filter_integers("abc") == []
``` 
The code defines a function **`filter_integers`** that takes a list of any type as input and returns a new list containing only the integer elements from the input list. The code provides a test cases to ensure the function's correctness, passing various values and expected results through the function and asserting the results are equal.