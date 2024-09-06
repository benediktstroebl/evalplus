```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded = ''
    
    for char in message:
        if char.isalpha():
            if char in vowels:
                encoded += alphabet[alphabet.find(char) + 2]
            else:
                encoded += char.swapcase()
        else:
            encoded += char
    
    return encoded
```

The Python script provided defines a function `encode` that takes a message as input. This function performs a series of transformations on the input message. It begins by defining two strings: `vowels` and `alphabet`. The `vowels` string contains all the vowels in the English alphabet, both in lowercase and uppercase. The `alphabet` string contains all the letters of the English alphabet, both lowercase and uppercase. 

The function then iterates through each character in the input message. If the character is a letter of the alphabet, it checks if it's a vowel. If it is, the function appends to `encoded` the letter that is two positions ahead of the original vowel in the `alphabet` string. This effectively replaces the vowel with its "alphabetical neighbor" that is two places ahead. If the character is not a vowel, the function instead appends the character, but converted to uppercase if it's lowercase or lowercase if it's uppercase, effectively swapping its case. 

Non-alphabetical characters remain unchanged as they are encountered during the iteration, and they are directly appended to the `encoded` string. 

The function returns the `encoded` string upon completion, ensuring that all letters in the input message have been appropriately encoded based on the rules described in the problem statement. 

This code demonstrates how Python's string manipulation capabilities and iterative processing can be leveraged to create a solution for the encoded message problem.