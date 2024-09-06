```python
from typing import List
def filter_integers(values: 
    return [x for x in values if type(x) == int]

values = ['a', 3.14, 5]
print(filter_integers(values))  # [5]

values = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values))  # [1, 2, 3]

values = [1, 2, 3, 'a', 4]
print(filter_integers(values))  # [1, 2, 3, 'a', 4]

values = List[1, 2, 3, 'abc']
print(filter_integers(values))  # [1, 2, 3]

``` 
This script defines a function **filter_integers** that takes a list of values and returns a new list that contains only the integers from the input list. 

It then demonstrates the use of the function with a variety of input lists, passing them through the function and printing the results to the console.