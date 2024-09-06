```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    l = list(set(l))
    l.sort()
    return l
```
This Python script defines a function unique that takes a list l as an argument and returns a sorted list of unique elements present in the input list. It does so by first converting the list into a set using the set() function, which removes any duplicate elements automatically. Then, it converts the set back into a list using the list() function, and finally, it sorts the unique elements in ascending order using the sort() method. 

The function includes a docstring that describes its purpose and provides an example of its usage. The example list provided in the docstring demonstrates how the function can be used, and the resulting output shows the sorted unique elements retained from the input list. 

To see the docstring and be able to execute this code, it is necessary to declare the function at the beginning of a Python file and execute it either using a debugger or by printing its result in an interactive session of Python.