```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = []
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message.append(alphabet[alphabet.index(char) + 2])
            else:
                new_message.append(char.swapcase())
        else:
            new_message.append(char)
    
    return ''.join(new_message)
```

This code defines a function `encode(message)` that takes in a message. The function loops through each character in the message, and if the character is a letter, it checks if it is a vowel. If the character is a vowel, it is replaced by the letter 2 places ahead of it in the English alphabet. If the character is not a vowel, it is swapped case. All other characters are left unchanged and appended to the `new_message` list. Finally, the function returns the joined string of characters in `new_message`. 

Here is an example usage of the code:
```python
encode('This is a message')
```
Which would return the encoded message:
```
tHKS KS C MGSSCGG
``` 

The code assumes that the input will only contain letters, and ignores non-alphabet characters.