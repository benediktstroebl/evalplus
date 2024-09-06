```python
def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    a = x + y
    b = x + z
    c = y + z

    if not isinstance(x) or not isinstance(y) or not isinstance(z):
        return False
    
    if a in [x, y, z] or b in [x, y, z] or c in [x, y, z]:
        return True
    
    return False
```

The function employs three variables to store the sums of all pairs of values to then check if they match any of the three original values. The function first checks if the integers criteria is met, and only then performs the equivalence check. 

Here is an example usage of the function:
```python
>> any_int(5, 2, 7)
True

>> any_int(3, 2, 2)
False

>> any_int(3, -2, 1)
True

>> any_int(3.6, -2.2, 2)
False
```

This should output `True` for the first example, `False` for the second, `True` for the third and `False` for the fourth.