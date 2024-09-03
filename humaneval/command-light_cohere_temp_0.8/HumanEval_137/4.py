```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if values are equal.
    """

    in_orders = [
        (1,2),
        (2,3),
        ("5","1"),
        (1,"6"),
        (6,"1"),
        (3,1)
    ]
    for a,b in in_orders:
        if type(a) == type(b):
            if a == b:
                continue
            print('Both are ', type(a))
        else:
            if isinstance(a, str):
                print('a is string ', type(a))
            else:
                print('a is integer ', type(a))
            if isinstance(b, str):
                print('b is string ', type(b))
            else:
                print('b is integer ', type(b))
            if a > b:
                print('a is greater ', end='')
            else:
                print('b is greater ', end='')
    return None
```