```python
def encrypt(s):
    """Create a function to encrypt a string with the alphabet rotated.
    alphabet shift is down two places.

    Args: 
        s (strring string)
        
    Returns: 
        encrypted string
    """
    s = ''.join(s)
    return s[::2]

# Test cases
test_encrypt = [
    ("hi", "lm"),
    ("asdfghjkl", "ewhjklnop"),
    ("gf", "kj"),
    ("et", "ix"),
    ("bcda", "tok"),
    ("zxcbr"),
    ("ttttt", "xx")
]

for test in test_encrypt:
    actual = encrypt(test)
    assert actual == test[1], "Encrypted text does not match the expected output"
```