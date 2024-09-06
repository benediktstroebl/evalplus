```python
def encode(message):
    vowels = 'aeiouAEIOU'
    swapped = ''.join(letter.swapcase() if letter.isalpha() else letter for letter in message)
    return swapped.translate(str.maketrans(vowels, vowels[2:] + vowels[:2]))
```

This code uses the `str.translate()` method to replace each vowel with the 2nd letter ahead of it in the alphabet (if that position is a vowel, it will replace it with the 3rd letter ahead, and so on). The `swapcase()` method is used to swap the case of all other letters. The code first checks if each character is a letter using the `isalpha()` method, and only swaps the case for letters, leaving non-letter characters unaffected.

To improve the readability of the code, I added some whitespace and indentation. The use of chains of methods and lists (e.g., `vowels[2:] + vowels[:2]`) makes the code more concise.