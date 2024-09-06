```python
def encode(message):
    vowels = 'AEIOUaeiou'
    swapped = ''.join(c.swapcase() if c.isalpha() and c not in vowels else (vowels.find(c) + 2) % 26 + chr(vowels.find(c) + 97) for c in message)
    return swapped
```

This script defines a function `encode` that takes a message as an input. It does the following:
1. Creates a variable `vowels` which is a string that contains all the vowels in the English alphabet.
2. Uses a list comprehension to iterate through each character in the `message`.
3. For non-vowel letters, swaps its case.
4. For vowel letters, replaces them with the letter that is 2 positions ahead of it in the English alphabet, and then adds the offset of 97 to the result to stay within the ASCII range. 

The script will convert messages to uppercase if all characters are letters and either all vowels or no vowels are present in the input. The decoding key for vowel replacement is always based on the English alphabet, which does not vary. 

This solution assumes that the input contains only letters. If the input may contain other characters, additional checks and handling are required. 

To test this script, you can call the `encode` function with a message as input, and it will return the encoded message according to the algorithm described.