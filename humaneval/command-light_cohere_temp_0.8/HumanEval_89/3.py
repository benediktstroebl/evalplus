```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    - alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    - Example string is passed as an argument, first check if it's a string.
    - alphabet is the string and then rotate each letter using a formula.
    - return the string encrypted
    """
    
    # test case
    test_string = "asdfghjkl"
    if isinstance(test_string, str):
        encrypted = encrypt(test_string)
        print(f"Original: {test_string}")
        print(f"Encrypted: {encrypted}")
        assert encrypted == "ewhubuntuop"
    else:
        print("Test string is not a valid string")
```