```python
def encrypt(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = []
    for char in string:
        index = alphabet.find(char)
       new_index = (index + 2 * 2) % len(alphabet)
        encrypted.append(alphabet[new_index])
    return ''.join(encrypted)
```
This function uses a loop to iterate through each character in the string, finding the index of each character in the alphabet, and then calculating the new index after a downshift of two multiplied by two places. If the new index is out of bounds for the length of the alphabet, it uses modular arithmetic to revert the index to a valid one. Finally, it appends the character at the new index to the `encrypted` list and returns the stringified list.

Here's an example function call:
```python
encrypt('hi') # returns 'lm'
```
```python
encrypt('asdfghjkl') # returns 'ewhjklnop'
```
```python
encrypt('gf') # returns 'kj'
```
```python
encrypt('et') # returns 'ix'
```