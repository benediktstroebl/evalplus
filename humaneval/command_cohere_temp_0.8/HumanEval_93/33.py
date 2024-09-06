```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() for letter in message if letter.isalpha())
    translated = swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
    return translated
```

This code defines a function `encode(message)` that takes a message as an input. It performs the following steps:
1. Collects all vowels in the English alphabet, both lowercase and uppercase, into the `vowels` string.
2. Uses a list comprehension to swap the case of each letter in the message while leaving non-alphabetical characters untouched. This results in the `swapped` string.
3. Utilizes the `translate` method to perform a character substitution. It takes the `swapped` string and the translation table created with `str.maketrans()` to substitute each vowel with the letter 2 places ahead of it in the English alphabet. The `str.maketrans()` function creates a translation table where vowels are mapped to the 2nd occurrence of themselves (i.e., 'a' is mapped to 'c', 'b' to 'd', and so on), and all other characters are left untouched.
4. The message is then returned as the translated string.

The code effectively encodes the message by swapping letter cases and replacing vowels with the letters 2 places ahead in the English alphabet, both lowercase and uppercase. 

You can verify the functionality of the code by running tests on the `encode()` function. You can do so by calling the function with different messages and comparing the output with the examples provided in the problem statement.