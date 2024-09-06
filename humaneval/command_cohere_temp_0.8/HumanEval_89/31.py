```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in s:
        index = alphabet.find(char)
       encrypted.append(alphabet[index+2*(index%2)::2])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each character in the input string. For each character, it finds its position in the alphabet, and then adds 2 to that position, alternating between adding 2 and adding 0 for the next position, to achieve the described encryption effect. It then builds the encrypted string by joining the encrypted characters together. The `join` method is used to concatenate the list of encrypted characters into a single string, which is then returned as the encrypted value.  This method is known as the Caesar cipher, which is a classical encryption technique. While this technique is relatively simple to decrypt, it would be difficult to do so without knowing the key, which makes it suitable for simple encryption tasks.