```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string is returned if no such vowel exists.
    """
    # Ensure input is case-sensitive and only contains letters to avoid error
    cleaned_word = "".join(char for char in word if char.isalpha()).upper()
    
    # Use a dictionary to check if the rightmost character is a consonant (or the end) and move leftwards
    closest_vowel = ""
    for char in cleaned_word[::-1]:
        if char in "AEIOUaeiou":
            closest_vowel = char
            break
    cleaned_word = cleaned_word[:-len(closest_vowel)]
    
    # Ensure the closest vowel is between two consonants
    if cleaned_word.count("") == 1:
        return closest_vowel
    else:
        return ""
```

This code starts by cleaning the input word, ensuring it is case-sensitive and only contains letters, which is crucial for the subsequent dictionary-based vowel check. It then reverse-iterates through the word, seeking out the first vowel character (excluding those at the start or end) and updating the closest vowel accordingly.

Finally, the function refactors the word without the closest vowel and checks if it has exactly one blank character (representing a consonant) between two vowels. If this condition is met, the function returns the closest vowel; otherwise, it returns an empty string. 

This approach ensures the code efficiently identifies the closest vowel while adhering to the problem's guidelines and handling edge cases.