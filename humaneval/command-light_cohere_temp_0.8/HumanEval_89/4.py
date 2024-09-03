Here is a Python script with a self-contained function that solves the problem of encrypting a given string:
```python
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
   
    alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    # Rotate the alphabet in a manner that shifts down by two multiplied places
    alphabet = 'abcdefghijklmnopqr'
    encrypted = [c if i % 2 == 0 else alphabet[i - 2] for i in s]
    return ''.join(encrypted)

# Unit tests
test_encrypt = []
test_encrypt.append('hi')
test_encrypt.append('asdfgjkl')
test_encrypt.append('gf')
test_encrypt.append('et')
test_encrypt.append('ewhjklnop')
test_encrypt.append('ix')

print("Unit tests:", end())

# Run the function and print the results of the unit tests
encrypt('test')
for result in test_encrypt
```