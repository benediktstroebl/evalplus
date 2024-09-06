Here's a Python script with a self-contained function that solves the decimal-to-binary problem according to the provided markdown code block:
```python
def decimal_to_binary(decimal):
    binary_string = '{0:b}'.format(decimal)
    return 'db' + binary_string + 'db'

# Example usage:
decimal = int(input("Enter a decimal number: "))
result = decimal_to_binary(decimal)
print(result)
```

You can use the function by providing a decimal number as a parameter. The function will return the binary representation of the number with '0' and '1' characters and extra 'db' characters as specified in the problem statement. Feel free to test the function with other decimal numbers!