```python
def encode(message):
    vowels = 'aeiouAEIOU'
    new_message = ''.join(
        c.upper() if c.isalpha() and c not in vowels else
        vowels.find(c) + 2 + vowels[vowels.find(c) + 1]
        for c in message
    )
    return new_message
```

This script defines a function `encode` that takes a message as an input. It iterates over each character in the message and makes the following transformations:
1. Leaves uppercase letters unchanged.
2. Leaves non-alphabetic characters untouched.
3. For alphabetic characters:
   - If the character is a vowel, it is replaced by the character that is two positions ahead of it in the English alphabet. This is achieved by finding the character's index in the string `vowels` and adding 2, and then finding the subsequent character.
4. The final encoded character is then converted to uppercase. 

The script returns the encoded message as the result. 

This problem can be solved in a variety of ways, this is just one possible solution. Let me know if the issue persists or if you'd like to discuss an alternative approach.