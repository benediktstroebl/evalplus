```python
from typing import List
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

#Test cases 

values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]

print("Test case 1: ", end="")
print(filter_integers(values1))
print("\n")

print("Test case 2: ", end="")
print(filter_integers(values2))
print("\n")
```
This script defines a function `filter_integers` that filters out any non-integer values from a given list. 

The function uses the typing feature in Python to define the `values` parameter as a list of any type, and then returns a new list of only integers using list comprehension. 

The script also includes two test cases, which pass the function the values1 and values2 lists, and print the resulting filtered lists.