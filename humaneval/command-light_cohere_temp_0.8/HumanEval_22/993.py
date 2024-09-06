```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [int(i) for i in values if i.isinstance(int)]
```
The code uses the isinstance() function from the typing module to check if each value in the input list is an instance of the int class, which is a special class in Python that represents integer numbers. The function then returns a list of the integers from the list.