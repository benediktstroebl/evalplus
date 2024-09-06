```python
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    # Find the first vowel character from the right side of the word
    for char in word[::-1]:
        if char in vowels:
            return char
    return ''
```

The Python script defines a function `get_closest_vowel()` as described in the prompt. It iterates through the characters of the reversed input word using a for loop. It checks if each character is a vowel (uppercase or lowercase). If a vowel is found, the function immediately returns that character. If no vowels are found, the function returns the empty string. 

This code will find the closest vowel to the right of the word, assuming the consonants are in the word's body and not at the very end. It will return the empty string if no such vowel is found. 

The total time complexity of this code is O(N), which makes it very efficient considering it iterates the word reverse only once.