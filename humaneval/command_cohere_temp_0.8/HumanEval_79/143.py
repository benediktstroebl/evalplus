Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bin_str = '{0:b}'.format(decimal)
    return 'db' + bin_str + 'db'

# Test cases
decimal = 15
result = decimal_to_binary(decimal)
print(f'Binary representation of {decimal} is {result}')

decimal = 32
result = decimal_to_binary(decimal)
print(f'Binary representation of {decimal} is {result}')
```

In the above code, `decimal_to_binary` function takes a decimal number as input and uses the format method of the string formatting class, which converts the number to a binary string representation. The prepend and append `db` ensure the binary string is returned as a valid markdown code block. 

The output of the code is:
```
Binary representation of 15 is db1111db
Binary representation of 32 is db100000db
```

This solution is self-contained and can be easily copied and run to test the behavior. Let me know if it works correctly!