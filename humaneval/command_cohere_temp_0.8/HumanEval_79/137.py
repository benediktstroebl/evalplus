Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes the tests:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format"""
    bib = []
    while decimal:
        bib.append(decimal % 2)
        decimal //= 2
    bib.reverse()
    return 'db' + ''.join(str(x) for x in bib) + 'db'

# Test Cases
assert decimal_to_binary(15) == 'db1111db'
assert decimal_to_binary(32) == 'db100000db'
```

This script defines the `decimal_to_binary()` function, which takes a decimal number as input and converts it to binary format. The function iterates through the decimal number, converting each digit to its binary representation and appending it to a list. Finally, the list of binary digits is joined into a string and prepended and appended with 'db' characters to ensure the desired binary format.

The test cases are also provided to verify the correctness of the function. You can use these test cases to validate the function's behavior against different input values.  If you encounter any issues or require further refinement, feel free to provide additional context or questions.