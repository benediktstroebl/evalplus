Here is a self-contained Python script that defines a function strlen that calculates and returns the length of a given string:
```python
def strlen(string: str) -> int:
    """ Return length of given string """
    return len(string)

# Test cases
assertEqual(strlen(''),             # empty string is zero len
    )
assertEqual(strlen('abc')),         # 'abc' has 3 characters, 2 spaces, and 1 tab...
    )

# Longer strings
assertEqual(strlen('ABC'),        # ABC has 5 characters
    )
assertEqual(strlen('abcdeutsch')), # abcdeutsch has 8 characters
    )

# Strings with special characters
assertEqual(strlen('∛¨')),        # Special characters are still valid
    )
assertEqual(strlen('\n\t\r\f!  # All valid ASCII characters
    )

# Input validation test
assert len(strlen('')) == 0,        
    "empty string should return 0 length"
```
This script defines a function `strlen` that calculates the length of a given string. It is then implemented with a number of test cases that cover different types of inputs and validate the correctness of the function.