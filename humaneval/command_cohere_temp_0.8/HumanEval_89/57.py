```python
def encrypt(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in s:
        index = alphabet.find(char)
       if index == -1:
            encrypted += char
        else:
            # Shift the index down two to get the new character
            new_index = index - 2 * (index % 2)
            if new_index < 0:
                new_index = 26 + new_index
            encrypted += alphabet[new_index]
    return encrypted
```
This function encrypts a string s by shifting each character's index in the alphabet down by two, and wrapping around to the opposite end if the index reaches the end or begins anew at the start of the alphabet. The function accomplishes this by dividing the current index by two, and then subtracting two, and using the modulo operator to ensure that the wrap-around occurs correctly.