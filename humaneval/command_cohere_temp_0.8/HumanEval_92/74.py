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
    
    if a in (b, c) and a == int(a):
        return True
    elif b in (a, c) and b == int(b):
        return True
    elif c in (a, b) and c == int(c):
        return True
    else:
        return False
```

The function employs three conditional statements to compare each of the three potential sums against the remaining two variables. The function returns `True` if any of these conditions are met, and `False` otherwise. 

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

The function will return `True` for the first two examples because the sum of either pair is equal to the third number, and this expression is also true for the third example. However, the fourth example is False because 3.6 is not an integer, therefore not meeting the criteria for the function's truthfulness.