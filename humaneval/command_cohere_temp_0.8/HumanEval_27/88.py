```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, applies the `swapcase()` method to flip the case. Non-alphabetic characters are directly appended to the new string.

To test this script, you can call the `flip_case` function with different input strings and compare the output with the expected result. Below is an example of how you can use this function with different inputs and expected outputs:
```python
print(flip_case('Hello'))  # Expected output: hELLO
print(flip_case('ÜPPÖ'))  # Expected output: ÜPPÖ
print(flip_case('123$&*'))  # Expected output: 123$&*
```

Ensure that you are running this code in a Python environment that supports Markdown code blocks and that the complete script above is present. Verify that the example outputs match the expected results mentioned in the comment above each print statement.