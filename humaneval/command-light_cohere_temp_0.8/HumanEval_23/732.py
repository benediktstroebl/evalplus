```python
def strlen(string: str) -> int:
    return len(string)

# Test the function
assert(strlen(''), equal=False)  # False, because empty string has length 0
assert(strlen('abc')), equal=False  # True, because string length is 3
```
This code defines a function `strlen` that calculates the length of a given string. It returns an integer value representing the specific length. The function is then tested using an `assert` statement, which verifies if the function correctly calculates the length of the given string. 

Note that, the `equal` argument is set to `False` since empty strings have a length of 0, which is not equal to any other value.