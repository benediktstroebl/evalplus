Here's a Python code block with a function `decimal_to_binary` that completes the described task:
```python
def decimal_to_binary(decimal):
    bin_str = "{0:b}".format(decimal)
    return "db"+bin_str+"db"
```

This method straightforwardly employs the `format` function's `b` specifier to translate the decimal integer to a binary string. The prefixing and suffixing "db" ensure that the result is in the desired format. 

Here's a sample output:
```
decimal_to_binary(15) == "db1111db"
```

And for larger numbers:
```
decimal_to_binary(32) == "db100000db"
```

This approach is both simple and efficient, rendering it an optimal solution for the problem at hand.