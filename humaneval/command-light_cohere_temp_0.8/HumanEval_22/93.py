```python
from typing import List
def filter_integers(values): 
    return [x for x in values if type(x) == int]

# Test the function
values1 = [1, 2, 3, 'abc', [], True]
values2 = [3.14, 5, 'hello']
values3 = [1, 2, 3]

print("Test 1: ", end="")
print(filter_integers(values1))
print()

print("Test 2: ", end="")
print(filter_integers(values2))
print()

print("Test 3: ", end="")
print(filter_integers(values3))
```
This Python code defines a function called `filter_integers` that filters a list of any Python values and returns a new list containing only the integers. It uses a same list comprehension to iterate over the values in the input list and checks if each value is an integer using the `type()` built-in function. The filtered list is then returned.