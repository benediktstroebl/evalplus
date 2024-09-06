```python
def encrypt(s):
    encrypted = ''
    rotating_letters = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'efghijnopqrstuvwxyzabcd')
    encrypted = s.translate(rotating_letters)
    return encrypted
```

This function uses the `str.maketrans()` method to create a translation table and then uses `str.translate()` to perform the encryption. An example of how this function can be used is `encrypt('hi')`, which returns 'lm'.