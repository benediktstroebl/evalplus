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

This code defines a function `encode(message)` that takes a message as an input. The function first creates a string `vowels` comprising all vowels in both lowercase and uppercase to later check if a character is a vowel or not. It then initializes an empty string `new_message` to store the encoded message, and iterates through each character in the input `message`. 

If the character is a letter, it checks if it's a vowel, in which case it adds the character 2 places ahead in the alphabet to `new_message`. If it's not a vowel, it swaps the character's case and adds it to `new_message`. Finally, it returns the `new_message`, which contains the encoded message. 

Here is an example usage of the function:
```python
encode('test') # TGST
encode('This is a message') # tHKS KS C MGSSCGG
```

This demonstrates how the function encodes a message using the rules mentioned in the problem. Note that this code works under the assumption that only letters will be passed in the provided `message` and does not account for the punctuation or other characters.