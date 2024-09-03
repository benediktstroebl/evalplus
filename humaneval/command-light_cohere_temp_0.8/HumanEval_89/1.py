```python
def encrypt(s):
    """Create a function to encrypt a string using a custom rotation scheme.
    Encryption scheme: shifts all letters down by twice and returns the rotated string.
    Args: 
        - string s to encrypt 
    Returns: 
        - the encrypted string
    """
    alphabet = 'abcdefghijklmnopqr'
    rotated_alphabet = [c[2:] + c[0] for c in alphabet]
    return ''.join(rotated_alphabet, s)

# Test suite
test_enc = {'hello': 'roOAalt!'}
test_dec = {'roOAalt!!'='encrypt('hello')

# expected output: {'hello': 'ello',}

print('test suite:')
print(test_enc)
print(test_dec)
``` 
This code defines an encryption function that uses a custom rotation scheme to encrypt a given string. It then creates a suite of tests that cover various strings and their corresponding encrypted and decrypted values.