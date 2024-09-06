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

This code defines a function `encode` that takes a message as an input. It then creates a new message string where it iterates over each character in the given input message. If the character is a letter (using the `isalpha()` function), it checks if it's a vowel. If it is, it converts it to a new character by moving two places forward in the alphabet (using the `ord()` and `chr()` functions). If it's not a vowel, it swaps the case of the letter using the `swapcase()` function. If the character is not a letter, it copies it as is into the new message. Finally, the function returns the new message as the encoded version of the input. 

This solution addresses the requirement of only swapping the case of letters and replacing vowels with the corresponding letters 2 places ahead in the alphabet.