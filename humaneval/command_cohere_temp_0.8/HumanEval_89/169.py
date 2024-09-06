```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for letter in s:
        # Find the index of the current letter in the alphabet
        index = alphabet.find(letter)

        # Move the letter two places down in the alphabet and add it to the list
        encrypted.append(alphabet[index - 2:index])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each letter in the input string. It first finds the index of the current letter in the alphabet, and then it shifts this letter down two places in the alphabet. Finally, the function rejoins the encrypted letters into a string and returns the result.

Here is a test to try out the function alongside its explanation:
```python
def test_encrypt():
    # Test string with more than one letter
    assert encrypt('hi') == 'lm'
    
    # Test string with many letters
    assert encrypt('asdfghjkl') == 'ewhjklnop'
    
    # Test string with only two letters
    assert encrypt('gf') == 'kj'
    
    # Test string with only one letter
    assert encrypt('et') == 'ix'
```
This test suite uses the `assert` statement to check if the encrypted value corresponds to the correct answer for different input strings.