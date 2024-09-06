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
1. It creates a variable `vowels` that stores all vowels in both lowercase and uppercase to be used for lookup.
2. It initializes an empty string `new_message` to store the encoded message.
3. It iterates through each character in the input message.
4. If the character is a letter, it checks if it is a vowel. 
   - If it is a vowel, it adds the character two places ahead in the alphabet to `new_message`.
   - If it is not a vowel, it swaps the case of the character and adds it to `new_message`.
5. If the character is not a letter, it adds the character as it is to `new_message`.

The script ensures that only letters are altered as specified in the problem statement, and other characters (like digits or special characters) are left unchanged. 

You can verify this by testing the script with the example inputs provided in the problem statement, as well as any other messages you wish to encode. 

Let me know if you need any adjustments, and I'll be happy to help!