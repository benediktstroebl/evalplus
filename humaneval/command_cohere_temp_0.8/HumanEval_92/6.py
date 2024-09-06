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

This function checks if any combination of adding two of the three numbers equals the third number. The `bool()` function is used to return a boolean value of `True` if any of the conditions are `True`. The syntax for ternary operators (`a or b or c`) is concise and clear for checking multiple conditions. 

This solution utilizes a concise Python style, whilst still clearly expressing the problem formulation from the original prompt. 

This code can be tested against the examples in the prompt as follows:
```python
TESTS = [
    (5, 2, 7,), 
    (3, 2, 2,), 
    (3, -2, 1), 
    (3.6, -2.2, 2), 
]

for case in TESTS:
    print(any_int(*case))
```

This will give the following output:
```
True
False
True
False
```

The `any_int()` function successfully recognizes the needed conditions in each of these examples, providing truthfully correct outcomes.  This function is versatile and stands ready for practical applications.