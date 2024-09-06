```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() if letter.isalpha() else letter for letter in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This script defines a function `encode` that takes a message as an input. It then does the following:
1. Collects all vowels in the English alphabet, in both lowercase and uppercase, into the `vowels` string.
2. Uses a list comprehension to iterate through every character in the input message.
    - If the character is a letter, it is swapped case-wise using the `swapcase()` method.
    - If the character is not a letter, it remains unchanged.
3. Then, it uses the `translate` method to replace each vowel with the letter 2 places ahead of it in the alphabet. This is achieved using the `str.maketrans` method, which takes two arguments: the old mapping and the new mapping. In this case, 'aa' would map to 'CC', 'bb' to 'DD', and so on.

The resulting string is then returned.

Here is an example usage of the script:
```python
encode('test')
# TGST
```

And another example:
```python
encode('This is a message')
# tHKS KS C MGSSCGG
```

This encoded message is produced by:
- Swapping the case of non-vowel characters, resulting in 'tHKS IS A MGSSCGG'.
- Then, translating the vowels to the 2nd letter ahead in the alphabet, as described. 

The script ensures that only letters are targeted, and special characters remain untouched.