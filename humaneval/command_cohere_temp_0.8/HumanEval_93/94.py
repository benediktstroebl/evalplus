```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    encoded = ''.join(vowels.index(char) + (26 if char in vowels else 1) for char in swapped)
    return encoded
```

This script defines a function `encode(message)` that takes a message as an input. It does the following:
1. Collects all vowels in the alphabet, both in lowercase and uppercase.
2. Uses a list comprehension to iterate through all characters in the message, swapping their case if they are letters.
3. Searches for the position of each character in the swapped message in the vowel list, indexing it on the list and then adding 26 if the character is a vowel, and 1 if not.
4. Returns the encoded message as the final output. 

Is there anything else I can help you with? Feel free to specify other coding problems or questions you have, and I'll do my best to provide self-contained solutions and explanations!