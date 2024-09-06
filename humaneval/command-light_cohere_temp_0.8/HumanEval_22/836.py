```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
print(filter_integers(values1))  # [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values2))  # [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 4, 5, 'abc', None]
print(filter_integers(values3))  # [1, 2, 3, 4, 5]
```

The function **filter_integers** takes a list of values and returns a new list containing only the integers. The function uses the filters the list values and checks if each element is an instance of **int**, then it adds it to the new list. 

To test the function, we can call it with a list of values and print the resulting list. The output will be the values.