Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bins = []
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bins.append(str(remainder))
    bins.reverse()
    return 'db' + ''.join(bins) + 'db'

# Examples:
print(decimal_to_binary(15))  # Outputs: db1111db
print(decimal_to_binary(32))  # Outputs: db100000db
```

This script adheres to the problem description provided. The `decimal_to_binary` function accepts a decimal number, converts it to binary format, and ensures the output adheres to the specified format by adding 'db' prefixes and suffixes. The provided examples output is also included to validate the correct behavior of the function.