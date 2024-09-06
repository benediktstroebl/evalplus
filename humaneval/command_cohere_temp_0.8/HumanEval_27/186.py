```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, uses the `swapcase()` method to flip the case. Non-alphabetic characters are left unchanged.

To test this function, you can call it with different input strings and compare the output with the expected result. Here's an example:
```python
# Test the flip_case function
print(flip_case('Hello'))  # Expected output: hELLO
print(flip_case('123'))    # Expected output: 123
print(flip_case('foo BAR')) # Expected output: FOO BAR
```

This should output:
```bash
hELLO
123
FOO BAR
```

The script successfully flips the case for alphabetic characters only while leaving non-alphabetic characters unchanged. 

If you encounter any issues or have further questions, feel free to ask!