```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This Python script defines a function unique that takes a list l as input and returns a sorted list of unique elements from l. Inside the function, a set seen is used to keep track of already-seen elements. The function then iterates over the input list, checking if each element is not in the seen set. If it hasn't been seen before, it is added to the set using the method provided by the condition not seen.add(element), and then included in the returned list. The function results are guaranteed to be sorted as the set operations do not alter the order of elements, and the returned list is automatically sorted when populated.

Here is an example of how to use the unique function:
```python
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```

This would output the following:
```
[0, 2, 3, 5, 9, 123]
``` 

The function unique can also be called in the same way as a regular function, with the input argument(s) passed after the function name, like this:
```python
unique([1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9])
```

This will return the unique elements from the list in unsorted order, which would be the following:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
``` 
Please note that the input list passed into the function unique must be a list or it will throw an error.

The code has a docstring which explains how the function works, and the format is consistent with the Python convention for docstrings. This makes the code easier to read and understand.

To execute the function and run the unit tests, an IDE or the Python command-line interface (CLI) can be used. The IDE will automatically find and run the tests within the code, whereas through the Python CLI, the command python -m unittest tests.py must be used. This will import the function unique and test the functionality of the script. 

Let me know if I can help with anything else!