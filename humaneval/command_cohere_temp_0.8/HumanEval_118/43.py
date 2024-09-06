```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    Ignores starting and ending vowels.
    """
    # Convert to lowercase for consistency and to ignore case
    word = word.lower()
    # Split the word on vowels to find general vowel positions and remove them
    # This also ensures starting and ending vowels are ignored
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = [c for c in word if c not in vowels]
    # If the word is empty, return an empty string immediately
    if not word:
        return ''
    # Split the word on spaces to get lists of consonants that may be sandwiched
    # between two consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    vowel_positions = [i for i, char in enumerate(word) if char in vowels]
    sandwiched_consonants = [
        consonants[i:] + [consonants[i + 1]]
        for i, char in enumerate(word)
        if char in consonants
        and ((i and vowel_positions[i - 1] < vowel_positions[i]) or
             (i + 1 < len(word) and vowel_positions[i + 1] < vowel_positions[i + 2]))
    ]
    # Return the closest vowel to the right of the word, preferring uppercase
    if sandwiched_consonants:
        return vowels[0].upper() if vowels[0].isupper() else vowels[0]
    return ''
```
This approach leverages list comprehension and Python's nifty string manipulation capabilities to provide a concise solution. Let's break it down:
1. **Lowercase Conversion**: The word is converted to lowercase to ensure the solution is case-insensitive and to make the problem constraints consistent. This also helps us ignore starting and ending vowels since they're not capitalized.
2. **Vowel Splitting**: The word is split on each vowel, which:
    - Identifies the word's vowel positions.
    - Helps us exclude starting and ending vowels.
    - Sorts the vowels to the left, contributing to the 'sandwich' effect we're looking for.
3. **Handling Empty Input**: A quick check ensures the manipulated word isn't empty. As per the problem, an empty result is returned if the word doesn't contain any vowels.
4. **Condensed Letter Splitting**: The word is split on spaces, and only consonants are considered. This is done to identify groups of consonants that could potentially be sandwiched between other consonants.
5. **Filtering Sandwich Cases**: A list comprehension filters instances where:
    - The current character is a consonant.
    - The character to the left is a vowel or another consonant (potential 'top' of the sandwich).
    - The character to the right is a vowel or another consonant (potential 'bottom' of the sandwich).
6. **Returning The Closest Vowel**: If any 'sandwiched' consonants are found, we return the closest vowel (preferring uppercase if all vowels are uppercase). If no vowels meet this condition, an empty string is returned. 

This solution is efficient and adaptable to edge cases provided the right validation is handled.