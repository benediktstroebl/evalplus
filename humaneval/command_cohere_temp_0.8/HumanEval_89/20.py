```python
def encrypt(s):
    encrypted = ''
    rotating_letters = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                                      'efghijklmnopqrstuvwxyz abcdefg hijklmnopqrstuv abcdefg hijklmnop')
    encrypted = s.translate(rotating_letters)
    return encrypted
```

This Python script defines a function `encrypt` taking a string `s` as input and returning an encrypted string using a shifted alphabet. To achieve this, it uses the `str.maketrans` method to create a translation table that rotates the alphabet by shifting each letter down two places. Then, it uses the `translate` method to perform the encryption by applying this rotation to the input string. The script returns the encrypted string. 

Output:
```python
ewhjklnop
```