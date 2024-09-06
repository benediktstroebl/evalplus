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

This code defines a function `encode` that takes a message as an input. It then does the following steps:
1. Defines a string `vowels` that contains all the vowels of the English alphabet in lowercase and uppercase (`'aeiouAEIOU'`).
2. Initializes an empty string `new_message` to store the encoded message.
3. Iterates through each character in the input `message`.
4. If the character is a letter:
   - If the character is a vowel, it calculates the ASCII value of the character plus 2 and then uses that value to convert it to a character, thus shifting the vowel two places forward in the alphabet. This is then appended to `new_message`.
   - If the character is not a vowel, it uses the `swapcase()` method to swap the case of the character, and the swapped character is appended to `new_message`.
5. If the character is not a letter (e.g., it's a digit or a symbol), it is appended directly to `new_message`.

Thus, the function converts vowels to the letters that are two places ahead of them in the alphabet while keeping other letters unchanged but swapping their case. The resulting encoded string is then returned.