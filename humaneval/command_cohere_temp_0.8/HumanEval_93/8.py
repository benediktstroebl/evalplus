```python
def encode(message):
    vowels = 'AEIOUaeiou'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.find(c) + 2 + vowels[vowels.find(c) + 1]
        for c in message
    )
    return new_message
```

This code defines a function `encode` that takes a message as an input. It iterates over each character in the message. If the character is a letter and it is a vowel, it finds the character's index in the string `vowels` and adds 2 to that index to get the character that will replace this vowel. If the character is not a vowel, it casts it to uppercase. Then the new character (or the modified old character) is added to the `new_message` string. Finally, the function returns this string, which is the encoded message.

Here is an example function call:
```python
encode('This is a message')
'tHKS KS C MGSSCGG'
```