```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test case 1
assert strlen('') == 0

# Test case 2
assert strlen('abc') == 3
```
This code defines a function `strlen` that calculates and returns the length of a given string. The function uses the fact method `len` to get the length of the string passed as an argument. 

The test cases ensure that the function works as expected, correctly calculating the length of the specified strings.