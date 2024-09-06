```python
def strlen(string: str) -> int:
    """ Returns length of the given string."""
    return len(string)

# Test case 1: empty string
assert strlen('') == 0

# Test case 2: alphabets
assert strlen('abc') == 3
```  This code defines a function strlen that calculates the length of a given string. It uses the `len()` function to return the length of the string. The function is then tested using the `assert` keyword with the test case 1(empty string) and test case 2 (alphabet string).