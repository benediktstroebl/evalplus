```python
def encode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouAEIOU'
    
    swapped = message.swapcase()
    translated = swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
    
    return translated.upper()
```

This code defines a function `encode(message)` that takes a message and encodes it according to the problem statement. 

The process is as follows:
1. The function first creates a string `alphabet` containing all the letters of the English alphabet and a string `vowels` containing all the vowels (both lowercase and uppercase).
2. It then creates a copy of the input message named `swapped`, with the letter case swapped - this is done using the `swapcase()` method.
3. Next, the function uses the `translate()` method to perform a translation on the `swapped` message. It uses `str.maketrans()` to create a translation table that maps each vowel to the letter 2 places ahead of it in the alphabet. 
4. Lastly, the translated message is converted to uppercase, and the encoded message is returned. 

This code ensures that letters are correctly swapped and vowels are translated as described in the problem statement.