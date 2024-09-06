Here's a Python script that solves the problem:
```python
def decimal_to_binary(decimal):
    """Converts a decimal number to its binary representation, with extra '0's and '1's for formatting."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join('1' if b else '0' for b in bins) + 'db'
```

This code defines a function `decimal_to_binary` that takes in a decimal number and converts it to its binary representation, with extra `0` and `1` digits provided for formatting. It iterates through the decimal number, dividing it by 2 until it becomes 0. It keeps track of the remainder from each division operation and reverses them to obtain the correct binary representation. The code then joins these remainders with '0's and '1's to create the binary string, with 'db' added at the beginning and end for formatting.