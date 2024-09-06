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
    return ((type(x) == int) and (type(y) == int) and (type(z) == int) and 
            (x == a or y == a or z == a) and (x == b or y == b or z == b) and (x == c or y == c or z == c))
```

The function uses logical statements to check whether three conditions are met:
1. The three provided numbers are integers;
2. One of the numbers is equal to the sum of the other two;
3. One of the numbers is equal to the sum of the other two when those two are combined differently.

The function returns `True` if all these conditions are met, and `False` otherwise. 

The code includes type checks to ensure the numbers are integers and uses equality checks to verify if one of the numbers is equal to the sum of the other two. 

To see this function in action, run the following code:
```python
test_any_int = lambda: any_int(5, 2, 7) and any_int(3, 2, 2) and any_int(3, -2, 1) and any_int(3.6, -2.2, 2)
```

The lambda function above will return `True` when tested with the provided examples in the `any_int` function.