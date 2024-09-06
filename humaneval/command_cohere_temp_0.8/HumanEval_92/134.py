```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y == z
    b = y + z == x
    c = x + z == y
    return bool(a or b or c)
```

This function evaluates three conditions, each of which checks whether a particular pair of the three integers is equal to the sum of the third. It then returns True if at least one of these conditions is True, and False otherwise. This should match the specification you provided.

Here is an example usage of the function with a truthy result:
```python
print(any_int(5, 2, 7))  # This should print True
```

And here is an example usage of the function with a falsy result:
```python
print(any_int(3, 2, 2))  # This should print False
``` 

This should help you to meet the problem criteria. Let me know if you have any questions!