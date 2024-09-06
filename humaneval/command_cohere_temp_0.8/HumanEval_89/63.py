```python
def encrypt(string):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_alphabet = ''.join(alphabet[i::2] for i in range(26))
    
    for char in string:
        if char.isalpha():
            char_code = alphabet.find(char)
            encrypted_code = encoded_alphabet[char_code::2]
            encrypted += encrypted_code
        else:
            encrypted += char
    
    return encrypted
```

This script defines the `encrypt` function, which takes a string as input and returns the encrypted string using the rotated alphabet scheme described in the problem statement. It works by creating an encoded alphabet with letters shifted down by two and two places. Then, it iterates through each character in the input string, encrypting only the alphabetical characters and appending the rest as is. The encrypted alphabetical characters are found by calculating their new encoded indices using the rotated alphabet and mapping them back to the original alphabet. The output is a string with the encrypted version of the input string, ensuring that only non-alphabetical characters are left untouched. 

To ensure that the output of the function is correct, a few edge cases should be tested. An example of such tests is provided below:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('thequickbrownfox') == 'tbewlnviuqmcorg'
    assert encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 'BFGHJKLMNTPVWXZYXWVUTRD'
    assert encrypt('1234567890') == '7890123456'
    assert assert encrypt('The quick brown fox') == 'Tbe egmn lfwx vtugbkjpqrn'

test_encrypt()
```

This block of code tests the `encrypt` function with different inputs, including edge cases, to ensure that the function returns the expected output.