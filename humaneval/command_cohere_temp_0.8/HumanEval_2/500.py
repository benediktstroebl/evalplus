```python
def truncate_number(number):
    """
    Return the decimal part of the number given as parameter.
    """
    return number - int(number)
```

This function takes a float as an input and returns the decimal part of the number by subtracting the integer part of the number (obtained by rounding down the input float to the nearest integer). This is done using the built-in `int()` function in Python. The operation `number - int(number)` isolates the fractional part of the number, which is intended to be returned. 

To test this function, you can call it with a float, and the output will be the decimal part of that number. For example:
```python
truncate_number(3.5)  # Expected output: 0.5
``` 

This will return 0.5, which is the decimal part of the original number. 

The function is self-contained, meaning it does not rely on any external variables or functions, and it can be easily imported and used in another Python script or application.  It also has clear documentation, including a description of the function's purpose, the argument it accepts, and the value it returns, which helps developers understand its usage and behavior.  If needed, you can add further documentation on the expected behavior of the input parameter 'number'.  This will help developers who might utilize your function in different use cases.