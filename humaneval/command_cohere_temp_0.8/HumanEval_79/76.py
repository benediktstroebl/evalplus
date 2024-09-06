Here's a Python script that solves the problem of converting a decimal number to a binary string, with the added constraint that the string should start and end with the two characters 'db'. 

```python
def decimal_to_binary(decimal):
    """
    Convert a decimal number to binary string, with 'db' at start and end.
    """
    binary = bin(decimal).replace('0b', '').replace('0', '1').upper()
    return 'db' + binary + 'db'

# Test cases
decimal_values = [15, 32]
for dec in decimal_values:
    test_case = decimal_to_binary(dec)
    print(f"Test case {dec}: expected 'db{binary}' got '{test_case}'")
```

In the function `decimal_to_binary`, we use the built-in `bin` function to convert the decimal number to a binary string. We then use some string manipulations to convert it to the desired format. The `replace` method is used to remove the initial '0b' and any '0' characters that follow, which would otherwise disrupt the desired 'db' format. The `upper()` method is used to ensure that the binary string has all uppercase characters, matching the requirement of the problem statement. 

The script also includes a set of test cases that check the output of the `decimal_to_binary` function against a known binary string. Note that the known binary strings are hard-coded in the `decimal_values` list and their conversion to the 'dbXXXdb' format is tested. 
```python
decimal_values = [15, 32]
for dec in decimal_values:
    test_case = decimal_to_binary(dec)
    print(f"Test case {dec}: expected 'db{binary}' got '{test_case}'")
``` 

These could be expanded to more thoroughly test the function; for example, testing other starting and ending binary digits than '1', testing different decimal numbers, or testing for incorrect input types. 
```python
# Testing other starting and ending binary digits
decimal_values = [15, 32]
binary_digits = ['1', '10']
for dec in decimal_values:
    for dig in binary_digits:
        test_case = decimal_to_binary(dec, dig='db'+dig+'db')
        print(f"Test case {dec}, {dig} expected 'db{binary}' got '{test_case}'")

# Testing other decimal numbers
decimal_values = [2, 100, 255]
for dec in decimal_values:
    test_case = decimal_to_binary(dec)
    print(f"Test case {dec}: expected 'db{binary}' got '{test_case}'")

# Testing incorrect input type
try:
    decimal_to_binary('not_a_number')
except TypeError:
    print("Error: Incorrect input type.")
```