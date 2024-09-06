```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + 2*(ord(char) // 2)]
        encrypted += char
    return encrypted
```
This function takes a string **s** as input and iterates through each character. It skips non-alphabetical characters. For alphabetical characters, the function rotates the character by 2 to the appropriate position in the alphabet and repeats this rotation for the character's codepoint divided by 2. The rotated character is then appended to the `encrypted` string, which is returned upon completion. 

Here is a basic test suite to ensure the function behaves as intended:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('hello world') == 'lcaw ot uvhzib'
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'defghijklmnopqrstuvwxyzabc'
```