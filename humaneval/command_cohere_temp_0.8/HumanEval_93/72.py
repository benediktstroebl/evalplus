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

It then creates a new empty string called `new_message` to store the encoded message. It iterates through each character in the input message using a loop. For each character, it checks if the character is a letter using the `isalpha()` function. If it's a letter, it finds its index in the `alphabet` string using the `find()` method.

If the character is also a vowel, it calculates a new index by either adding 1 (for AAIOU) or 2 (for aeiou) using conditional checking, and then it appends the character from this new index to the `new_message` string. If the character is not a vowel, it appends the character as-is without any changes. Finally, after processing all characters, it returns the `new_message` string containing the encoded message.