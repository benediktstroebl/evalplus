Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join(str(x) for x in bins) + 'db'

# Examples:
print(decimal_to_binary(15))   # prints "db1111db"
print(decimal_to_binary(32))   # prints "db100000db"
```

This script defines a function `decimal_to_binary` that takes a decimal number as input and converts it to its binary representation, with extra 'db' characters as specified in the problem statement. The function divides the input by 2 repeatedly until it becomes 0, and keeps track of the remainder values (which represent the binary representation) in a list. Finally, the list of remainders is joined together to form the binary string, with 'db' added at the beginning and end for formatting.