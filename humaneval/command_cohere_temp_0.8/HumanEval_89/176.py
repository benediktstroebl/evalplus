```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each character in the input string s. It finds the character's index in the alphabet, then calculates the new index after a two-position shift. The new index is found by adding 2 * 2 to the current index and taking the modulus of the length of the alphabet. The character is then appended to a list, which is joined into a string afterwards. 

To ensure the correctness of the script, it is recommended to unit test the encrypt function with various input cases. Here is a suggested unit testing framework using pytest:
```
pytest -v 

# Test the encrypt function with the following inputs:
def test_encrypt_str(self):
    assert encrypt('hi') == 'lm'
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    assert encrypt('gf') == 'kj'
    assert encrypt('et') == 'ix'

def test_encrypt_empty_string(self):
    assert encrypt('') == ''

def test_encrypt_punctuation(self):
    assert encrypt('!@#$%^&*()') == ';qwediazayb'
    assert encrypt('?') == 'cd'
```
These tests check the correctness of the `encrypt` function for various input cases. Adjust the encryption logic if any of these tests fail.  For a better understanding of the encryption algorithm, you can uncomment the print(char, index, new_index) statement inside the loop in the encrypt function.  This will help you to visualize the process of shifting the alphabet.