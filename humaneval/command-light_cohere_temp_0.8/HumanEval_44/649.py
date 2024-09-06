```python
def change_base(x: int, base: int):
    """
    Change the numerical base of input number x to base B.
    return string representation after conversion.
    base numbers other less 10
   
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    >>> change_base(123, 5)
    TraceError: unsupported operand type(123)
    """
    if x < 0 or base < 2:
        raise ValueError("Input value x and base are invalid.")
    try:
        result = ''
        while x > 0:
            result = result + str(x % base)
            x = x // base
        return result
    except ZeroDivisionError:
        return "Input value x can't be zero"

def test_change_base():
    try:
        print(change_base(8, 3))
        print(change_base(8, 2))
        print(change_base(7, 2))
        print(change_base(123, 5))
        print(change_base(-7, 2))
        print(change_base(0, 15))
        print(change_base(-10, 1))
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

test_change_base()
```