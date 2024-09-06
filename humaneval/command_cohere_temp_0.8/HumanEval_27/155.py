```python
def flip_case(string: str) -> str:
    return ''.join(c.swapcase() if c.isalpha() else c for c in string)
```

This script provides a function that accepts a string as an argument and returns a new string where all lowercase characters are flipped to uppercase and all uppercase characters are flipped to lowercase. This is achieved by using a list comprehension that checks if each character is alphabetic using the `isalpha()` string method, and if so, uses the `swapcase()` method to flip the case. Non-alphabetic characters are left unchanged. 

To test this function, you can run the following code:
```python
test_str = 'Hello, World!'
expected_result = 'hELLO, wORLD!'

result = flip_case(test_str)

assert result == expected_result
```

This will ensure that the function produces the desired result when given a mixed-case string. 
The code defines a function that flips the case of alphabetic characters in a string, and leaves non-alphabetic characters unchanged. It uses a list comprehension to process each character in the input string. The `swapcase()` method is used to flip the case of alphabetic characters, while non-alphabetic characters like punctuation or spaces are preserved in their original form. The result is a new string with flipped case for letters and unchanged characters for non-letters.