```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    encrypted = ''
    for char in s:
        if char.isalpha(): 
            char = chr(ord(char) - 2 * ((ord(char) - 96) % 26))
        encrypted = encrypted + char
    return encrypted
```

This encrypt function takes a string **s** as input and returns a string encrypted with the alphabet rotated. It checks if each character is alphabetic, and if so, it subtracts 2 multiplied by the difference between the character's ASCII value and 96 from the character's ASCII value to encode it. A decryption algorithm could simply reverse the process to recover the original plaintext. 

Here is a simple test to ensure the function is working as expected:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
```

Ensure that all tests pass with a single command:
```python
python -m pytest
``` 
This will run the test file and display results, confirming that the script's encrypt function operates according to expectation.