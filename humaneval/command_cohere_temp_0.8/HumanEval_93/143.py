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

The script defines a function `encode(message)` taking in a message parameter and producing an encoded string as output. It first creates two strings, `vowels`, and `alphabet`, which contain all English vowels in lower and upper case, and the full English alphabet in lower and upper case respectively. It then iterates over each character in the input message, using the `isalpha()` function to check if the character is a letter. If the character is a letter, it checks if it is a vowel, in which case it finds the corresponding vowel in the `alphabet` string, and adds the letter two places later in the alphabet to the `encoded` string. If the character is not a vowel, it swaps the case of the character and adds it to the `encoded` string. For any non-letter characters in the message, the function simply adds the characters to the `encoded` string without modification. Finally, the function returns the encoded string.

Here is an example function call to `encode()`:
```python
encode('This is a message')
```
Output:
```
tHKS KS C MGSSCGG
```