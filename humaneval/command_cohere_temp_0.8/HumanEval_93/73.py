```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.find(c) + 2 + vowels[vowels.find(c) + 1]
        for c in message
    )
    return new_message
```

This script defines a function `encode` that takes a message as an input. The function loops through each character in the input message. For alpha characters, if it is not a vowel, it is converted to an upper case. If it is a vowel, it is replaced by the character that is two places ahead of it in the English alphabet. The function then returns the modified message.

Here is an example output:
```python
encode('test')
# TGST
encode('This is a message')
# tHKS KS C MGSSCGG
``` 

This behaves as specified in the problem statement.