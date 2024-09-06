```python
def encrypt(s):
    encrypted = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.isalpha():
            char = alphabet[alphabet.index(char) + 2*2]
        encrypted += char
    return encrypted
```
This function uses a loop to iterate through each character in the input string `s`. When it encounters an alphabetic character, it uses the index of that character in the alphabet to determine its position after the rotation. The index is incremented by 2 (downward shift of two steps) and then by another 2 (i.e., multiplied by 2) to determine the character's new position in the rotated alphabet. The character is then replaced with the character at this new position in the alphabet, and the encrypted string is returned.

Here's a test drive function to test the encrypt function with different input strings:
```python
def test_encrypt():
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'
    assert encrypt('fooBAR') == 'przgooMb'
    assert encrypt('abcdefghijklmnopqrstuvwxyz') == 'bfedkjlqnrxteeuvwsazmop'
``` 

You can run this test drive function to verify that the encrypt function behaves as expected with various input strings.