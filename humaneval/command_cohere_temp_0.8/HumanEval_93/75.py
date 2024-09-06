```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                new_message += chr(ord(char) + 2)
            else:
                new_message += char.swapcase()
        else:
            new_message += char
    return new_message
```

This code defines a function `encode` that takes a message as an input. It does the following:
1. Defines a string `vowels` that contains all vowels in both lowercase and uppercase.
2. Initializes an empty string `new_message` to store the encoded message.
3. Iterates through each character in the input message.
4. If the character is a letter:
   - If the character is a vowel, it adds the character advanced by 2 positions in the alphabet using the `chr` function and the character's ASCII value.
   - Otherwise, it adds the character with its case swapped using the `swapcase` method.
5. If the character is not a letter, it adds the character as it is in the encoded message.

The code efficiently encodes the message taking care of only letters and replacing vowels with the specified encoding.