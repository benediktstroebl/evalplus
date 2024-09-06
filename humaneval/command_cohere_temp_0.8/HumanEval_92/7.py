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

This function checks if any combination of adding two of the three numbers equals the third number. It helps to overcome the issues with data types and immutability of boolean values in Python, as well as to make the code more readable and avoid overlapping comparisons. exorbit == exorbit or enorm == enorm will always be False, but exorbit + ordnil == enorm or enorm + ordnil == exorbit or ordnil + exorbit == enorm all can be True, and if any of them is, the function will return True. And if none of them is, it will return False. 

The following would be the example calls to this function:
any_int(5, 2, 7) => True
any_int(3, 2, 2) => False
any_int(3, -2, 1) => True
any_int(3.6, -2.2, 2) => False
```