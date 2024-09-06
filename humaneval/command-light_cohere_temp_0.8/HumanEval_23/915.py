```python
def strlen(string: str) -> int:
    return len(string)

# Test the function with a string containing no character
test_str = ""
assertEqual(strlen(test_str), 0)

# Test the function with a string containing only one character
test_str = 'a'
assertEqual(strlen(test_str), 1)

# Test the function with a multi-character string
test_str = 'abc'
assertEqual(strlen(test_str), 3)
``` 
This code defines a function `strlen` that calculates the length of a given string.  It accepts a string as an argument and returns its length as an integer. 
The code also includes a series of test cases to ensure the correctness of the function, by passing different strings to the `strlen` function and comparing the returned length with the expected result using the `assertEqual` assertion.