```python
def change_base(x: int, base: int) -> str:
    """
    Change the base of the given number x to base b.
    Use string representation after conversion.
    base numbers are strings are either 10 or 2.
    """
    return ''.join('10' if base < 2 else '2')

    """
    # cast integer x to string to be able to perform integer-string conversion
    return ''.join(str(x), base)

x = int('8')
y = change_base(x, 2)
print(y)  # this will print "1000"

x = int('8')
y = change_base(x, 10)
print(y)  # this will print "22"

x = int('7')
y = change_base(x, 2)
print(y)  # this will print "111"

```
This function change_base takes two parameters, x (the number to be converted) and base (the desired base to convert to). the original number). The function returns a cast to string, and then uses the str.overall number format function with the str.so string representation of the time is performed by concatenating the original number with the base as specified by the function. The result is then returned as a string. 

This code is self-contained, and can be used to convert a number to a specified base. It can also be easily tested by passing the desired base and checking the output of the function.