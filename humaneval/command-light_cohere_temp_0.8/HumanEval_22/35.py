```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test the function with different input values
print(filter_integers(['a', 3.14, 5]))        # [5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, -10, 20, 0, '123']))  # [10, 0]
print(filter_integers([1, 2, 'abc', 3, '456']))  # ['1', '2', 'abc']
``` 
This code defines a function `filter_integers` that takes a list of values and returns a new list containing only the integer elements from the original list. 

The function utilizes the typing feature to define the return type as `List[int]`, indicating it should create a list of integers. 

Finally, the function is tested with various input values, and the expected output is printed.