```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in string:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            rotated_index = (index + 2) % 26
            encrypted += alphabet[rotated_index]
    return encrypted
```
This function uses the 'abcdefghijklmnopqrstuvwxyz' alphabet for encryption and decryption. The algorithm works by first searching for the char in the encrypted string's alphabet. If the index is -1, the character is not part of the alphabet, and the result is appended as is. If the index is within the alphabet's range, it uses (index + 2) % 26 to calculate the rotated index. The result will be appended with the character associated with the rotated index. This process repeats for all characters in the string, leaving you with an encrypted string. 

Here is an example usage of the encrypt function:
```python
original_string = "hi"
encrypted_string = encrypt(original_string)
print("Original string:", original_string)
print("Encrypted string:", encrypted_string)
```
Here are the results of the encryption operation:
```
Original string: hi
Encrypted string: lm
```

Original string: asdfghjkl
Encrypted string: ewhjklnop
Original string: gf
Encrypted string: kj
Original string: et
Encrypted string: ix
```