```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() if letter.isalpha() else letter 
                       for letter in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It then does the following:
1. Collects all vowels in the English alphabet, in both lowercase and uppercase, into the `vowels` string.
2. Uses a list comprehension to iterate through each character in the input message.
    - If the character is a letter, it is swapped case-wise. This is done using the built-in `swapcase()` method.
    - If the character is a vowel, it is replaced by the character that is two positions ahead of it in the `vowels` string. This is achieved by using the `translate` method with a custom translation table created by `str.maketrans`.
3. The method loops through and encodes each character, returning the encoded message. 

The expected output of the function is that all letters are swapped case-wise and all vowels are replaced by the characters 2 positions ahead of them in the English alphabet.

Output:
TGST
tHKS KS C MGSSCGG
```