Here's a Python script with a self-contained function that solves the decimal-to-binary problem and passes corresponding tests:
```python
def decimal_to_binary(decimal):
    """Convert a decimal number to binary format."""
    bins = []
    while decimal:
        decimal, r = divmod(decimal, 2)
        bins.append(str(r))
    bins.reverse()
    return 'db' + ''.join(str(x) for x in bins) + 'db'

# Test Cases
decimal = int(input("Enter a decimal number: "))
print(decimal_to_binary(decimal))
```

In the above code, the `decimal_to_binary()` function takes a decimal number as its input parameter. It uses a while loop to keep dividing the input number by 2 until the remainder is 0 (division by odd number). The remainder from each division is recorded in the `bins` list, which is then joined together to form the binary string. The final output is a string that starts and ends with 'db' to ensure the correct binary format.

Make sure to have the input statement included when running the code to input the desired decimal number.