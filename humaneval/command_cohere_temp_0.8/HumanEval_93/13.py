```python
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    new_message = ''
    
    for char in message:
        if char.isalpha():
            index = alphabet.find(char)
            new_index = (index + 1) if char in vowels else index + 2
            new_message += alphabet[new_index]
        else:
            new_message += char
            
    return new_message
```

This Python script defines a function called `encode` that takes a message as an input. Inside the function, it initializes two strings: `alphabet` containing the English alphabet and `vowels` containing all vowels. 

It then creates a new empty string called `new_message` to store the encoded message. It iterates through each character in the input message using a loop. For each character, it checks if the character is a letter using the `isalpha()` method. If it's a letter, it finds its index in the `alphabet` string using the `find()` method. 

If the character is also a vowel, it calculates a new index by either adding 1 (for vowels) or 2 (for consonants) to the current index, using conditional logic. It then appends the character at this new index to the `new_message` string. If the character isn't a letter, it directly appends the character to the `new_message` without any changes. 

Finally, after processing all characters in the message, the function returns this modified encoded string. 

The script ensures that only letters are affected by the encoding, while keeping non-letter characters unchanged in the encoded message.