```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'three', ())
values2 = [3.14, 5, 'abc', 7]
values3 = [1, 2, 3]
values4 = [1, 2, 3, 'four']
values5 = [True, False]

print("Test case 1: ", end="")
print(filter_integers(values1))
print()

print("Test case 2: ", end="")
print(filter_integers(values2))
print()

print("Test case 3: ", end="")
print(filter_integers(values3))
print()

print("Test case 4: ", end="")
print(filter_integers(values4))
print()

print("Test case 5: ", end="")
print(filter_integers(values5))
``` 
This script defines a function called `filter_integers` that takes a list of values as input and returns a new list that contains only the integers from the original list. The function uses the` isinstance(x, int)` function to check if each element in the input list is an integer. 

You can use this function to filter integers from a list of any python value, passing the list as an argument to the function.