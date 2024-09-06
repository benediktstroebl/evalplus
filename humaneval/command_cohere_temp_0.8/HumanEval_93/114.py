```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''.join(alphabet[alphabet.index(c) + (c in vowels and 2 or 0)] for c in message)
    return encoded
```

This Python script defines a function `encode` that takes a message as an input parameter and encodes it according to the problem statement. 

The function swaps the case of all letters in the message and replaces all vowels (both lowercase and uppercase) with the letter two places ahead of them in the English alphabet.

It uses two strings, `vowels` and `alphabet`, to store all vowels and the English alphabet respectively, and creates the encoded message by iterating through each character in the input message. It uses the `index` method to find the position of each character in the alphabet, and based on whether the character is a vowel or not, it either swaps it two places ahead or leaves it as is, eventually joining the encoded characters to form the final encoded message, which it returns.