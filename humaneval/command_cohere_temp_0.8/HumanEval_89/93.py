```python
def encrypt(s):
    encrypted = []
    for letter in s:
        if letter.isalpha():
            offset = letter == 'z' or letter == 'Z'
            encrypted.append(chr((ord(letter) - 96 - offset) % 26 + 96 + offset))
        else:
            encrypted.append(letter)
    return ''.join(encrypted)
```

This function takes a string as input and returns a string encrypted using the shifted alphabet described in the prompt. It iterates through the input string and for each character, it checks if the character is alphabetical. If it is, the function applies the encryption algorithm described in the prompt, which involves calculating an offset that depends on whether the character is 'z' or 'Z', shifting the character by 96 positions down the alphabet, and wrapping around to the beginning of the alphabet, and then adding the offset again to ensure the wrapped character is still shifted correctly. The character is then appended to the `encrypted` list after being converted to its encrypted form. If the character is not alphabetical, it is appended to the `encrypted` list as is. Finally, the function joins the encrypted characters together into a single string and returns the result. 

Here is a simple test to check if the function encrypt returns the expected output:
```python
TEST_STRINGS = [
    'hi', 'asdfghjkl', 'gf', 'et'
]

EXPECTED_ENCRYPTED = [
    'lm', 'ewhjklnop', 'kj', 'ix'
]

for test_str, expected in zip(TEST_STRINGS, EXPECTED_ENCRYPTED):
    assert encrypt(test_str) == expected
``` 

This test checks that the encrypted output for four different input strings matches the expected output as described in the prompt.