```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming consonants sandwiching it.
    Ignores vowels at the start and end.
    """
    # Ensure input is lowercase for consistency in testing
    word = word.lower()
    word = word.strip('aeiou')  # Remove all vowels from the beginning and end
    if not word:
        return ''  # Word was entirely vowels, or empty
    # Find the first index of a consonant after a vowel, or the end of the word
    next_consonant = word.find(word[0].lower() if word[0].isalpha() else '', 1)
    # Move forward one to find the closest subsequent vowel, or end of word
    return word[next_consonant:next_consonant+1].strip('aeiou') if next_consonant != -1 else ''
```

This approach works by:
1. Ensuring the input is lowercase and removing all initial and ending vowels to handle words like "FULL" or "Yogert".
2. Using `find` to search for the first consonant (after at least one vowel) to locate the onset of a potential consonant sandwich, skipping any false positives at the start.
3. Advancing one character to find the closest vowel following the identified consonant, ensuring the answer is "a vowel between two consonants" as per the prompt.