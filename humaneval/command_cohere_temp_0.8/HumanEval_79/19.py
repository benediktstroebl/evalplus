Here's a Python code block that contains a function called `decimal_to_binary` which takes a decimal number as input and returns the binary representation of that number with extra characters 'db' at the start and end of the string for formatting purposes.

```python
def decimal_to_binary(decimal):
    bin_str = "{0:b}".format(decimal)
    return "db{0}db".format(bin_str)
```

In the function, the `format` function is used to convert the binary representation of the decimal number to a string, and `format` again converts this string to have 'db' at the start and end of the string.