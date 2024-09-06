```python
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    res = ''
    for char in message:
        if char.isalpha():
            char_idx = alphabet.find(char)
            new_char_idx = (char_idx + 2) % 26 + alphabet[0]
            new_char = alphabet[new_char_idx]
            res += new_char if new_char in vowels else char
        else:
            res += char
    return res
```

The encode function takes a message and performs the desired encoding steps to create a new string. It uses a loop to traverse each character in the input message. For alphabetic characters, it does the following:
1. Finds the index of the character in the English alphabet.
2. Calculates a new index by adding 2 and taking the modulus 26 to wrap around within the range of the alphabet.
3. Finds the character at the new index, considering wraparounds.
4. Replaces the character with the new one if it's a vowel (from the vowels string). Otherwise, it keeps the original character. 
5. Appends the newly formed character to the result string. 

This encoding logic transforms the input message in the specified manner, and the resulting string is returned by the function.  The overall complexity is O(n), where n is the length of the input message.