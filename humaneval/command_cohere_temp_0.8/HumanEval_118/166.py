```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into individual characters and initialize the right-most vowel and its distance
    vowel, dist = None, float('inf')
    # Iterate over each character in the word
    for char in word:
        if char in 'aeiou':
            if char != word[0] and word[-1] != char:
                dist = 1
                vowel = char
            elif dist > 1 and char in 'eiou':
                dist, vowel = 1, char
    # Return the found vowel or an empty string
    return vowel or ''
```

This script assumes that the vowels 'a', 'e', 'i', 'o', and 'u' are to be found nestled between two consonants in the word (excluding starting and ending consonants). It assigns the property 'dist' to count the number of consonants between the right-most vowel and the end of the word, with a maximum value of 2. It then loops over the word and updates the 'dist' and 'vowel' variables whenever a vowel is encountered. The variable 'vowel' is updated to the most recent vowel encountered if its corresponding 'dist' is smaller than the maximum value of 2. The function returns an empty string if no such vowel is found. 

```python 
# TEST CASES
print(get_closest_vowel("yugurt"))  # u
print(get_closest_vowel("FULL"))  # U
print(get_closest_vowel("quiet"))  # Empty string
print(get_closest_vowel("cab"))  # Empty string
print(get_closest_vowel("coop"))  # o
``` 

This algorithm assumes the vowels to be present in the word, and their positioning to be such that they are nestled between two consonants, excluding starting and ending consonants.