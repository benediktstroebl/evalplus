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
This function uses a loop to iterate through each character in the input string `s`. It finds the character's index in the alphabet, then calculates a new index by adding 2 (to shift down) and multiplying by 2 (to shift back to the beginning), and taking the modulus of the length of the alphabet to handle wraparounds. It then appends the character at this new index to the `encrypted` list, which is joined into a string to return the encrypted message. 

Here's an example function call:
```python
encrypt('hi') # Returns 'lm'
```
This call will return 'lm', as the 'h' character's index in the alphabet is 4, and adding 2 twice and taking the modulus of the length of the alphabet results in a new index of 4, corresponding to the character 'l'. Similar processes are undertaken for the 'i' character to result in an 'm' character. 

Here's another example function call:
```python
encrypt('asdfghjkl') # Returns 'ewhjklnop'
```
This call results in 'ewhjklnop' because the first character 'a' is at index 97 (0-based) in the alphabet. Adding 2 twice and taking the modulus results in a new index of  0, corresponding to the character 'e'. This process is repeated for each character, resulting in the encrypted output of 'ewhjklnop'.