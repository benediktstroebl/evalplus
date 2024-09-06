Here is a Python script with a self-contained function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string """
    return len(string)

# Test cases
assertEqual(strlen(''),             # empty string
        0)

assertEqual(strlen('abc'),       # single character
        3)

assertEqual(strlen('abcabc')),    # two characters
        4)

assertEqual(strlen('abcabcabc')), # three characters
        4

# Additional test cases
assertEqual(strlen(''), 'too long') # empty string
assertEqual(strlen(123), int(123)) # converted string to int
```

Note: This code uses the `assertEqual` function to test the `strlen` function with various inputs, passing the output of the `strlen` function to the `assertEqual` function. The function `len` exactly matches the input to output, and raises an error if the test fails.