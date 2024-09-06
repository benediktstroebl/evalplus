```python
def encrypt(string):
    encrypted = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotate_len = 2
    step = 2

    for char in string:
        index = alphabet.find(char)
        new_index = (index + rotate_len * step) % len(alphabet)
        encrypted += alphabet[new_index]
    return encrypted
```

This Python script defines a function `encrypt` that takes a string as input and returns an encrypted version of that string, using a rotated alphabet to perform the encryption. 

The alphabet employed is stored in the `alphabet` variable and consists of `abcdefghijklmnopqrstuvwxyz`. This character set represents all lowercase English letters. A rotational element, `rotate_len`, is set to 2, indicating that each character in the alphabet will be shifted forward by two positions. The `step` variable, also set to 2, specifies the iteration interval for the alphabet's iteration.

The function's for loop iterates through the input string `char` by `char`. Within the loop, the current character's index within the `alphabet` is ascertained through the `find()` method. The `find()` method returns the index of the first occurrence of the character. Subsequent to this, the index is rotated forward by `rotate_len` positions multiplied by `step` intervals. This resulting index is then modulated by the length of the `alphabet` to ensure the rotation doesn't exceed the alphabet's bounds. The rotated index is used to append the corresponding character to the `encrypted` string, which aggregates the encrypted characters. Lastly, the function returns the `encrypted` string, concluding the encryption process. 

This approach results in an encrypted string where letters shift down by two positions multiplied by two places each time. 

Let's apply it to some examples: 
```python
print(encrypt('hi')) # Output: lm
print(encrypt('asdfghjkl')) # Output: ewhjklnop
print(encrypt('gf')) # Output: kj
print(encrypt('et')) # Output: ix
```

This showcases the encryption process where the 'hi' string encrypts to 'lm', 'asdfghjkl' encrypts to 'ewhjklnop', 'gf' encrypts to 'kj', and 'et' encrypts to 'ix'. 

This approach offers a straightforward method for encrypting letters using a rotated alphabet and can be tailored to fit more sophisticated encryption requirements.