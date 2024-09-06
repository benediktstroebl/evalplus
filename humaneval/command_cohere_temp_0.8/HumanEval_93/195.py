```python
def encode(message):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                res += alphabet[alphabet.find(char) + 2]
            else:
                res += char.swapcase()
        else:
            res += char
    return res
```

This code defines the `encode` function, taking a message as an input and encoding it according to the problem statement. 

The process involves several steps:
1. It creates two auxiliary strings: `vowels` and `alphabet`, which store all vowels and all letters of the English alphabet, respectively.
2. It initializes an empty string `res`, which will store the encoded message.
3. It iterates through each character in the input message.
4. For alphanumeric characters, it checks if the character is a vowel or not. If it is a vowel, it replaces the vowel with the letter that is 2 positions ahead of it in the alphabet. This is achieved by finding the index of the current vowel in the `alphabet`, and then adding 2 to that index to get the index of the replacement letter.
5. If the character is not a vowel, it swaps the case of the character and adds it to the `res` string.
6. For non-alphabetic characters (e.g., punctuation), it directly adds the character to the `res` string without any modification.

Overall, the code cleverly encodes the message by swapping case for consonants and substituting vowels with letters 2 positions ahead in the alphabet, all in a single pass.

You can verify the functionality of the code by running some tests with example inputs and comparing the encoded outputs with the ones provided in the problem statement.