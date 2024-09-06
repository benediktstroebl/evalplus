```python
def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end of the word are excluded.
    Empty string is returned if no eligible vowels are found.
    
    Args:
        word (str): Input word
    
    Returns:
        str: Closest vowel char or empty string if none are found
    """
    # Ensure input is case-sensitive and English alphabetic only
    assert all(char in 'abcdefghijklmnopqrstuvwxyz' for char in word), 'Input must contain only English letters.'
    
    # Define valid vowels and consonants for filtering
    vowels, consonants = set('aeiouAEIOU'), set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    closest_vowel = ''
    
    # Check if word has at least 2 characters (to have 1 consonant to separate the vowels)
    if len(word) < 2:
        return closest_vowel
    
    # Iterate through right-most characters (assuming word is right- padded with spaces)
    for char in word[-1]:
        if char in vowels:
            if not consonants or char in consonants:
                closest_vowel = char
                break
            consonants.remove(char)
        else:
            consonants.add(char)
    
    return closest_vowel
```

This approach focuses on removing consonants from the set of possible vowels as it iterates through the right-most characters in the word. The right-most character is checked for each character in the word, with the process halting when a vowel is discovered or all characters are checked. The method is case-sensitive, ensuring that the solution adheres to the problem's specifications. 

To mitigate any edge cases that may arise, remember to adapt the test cases to cover scenarios like one-letter words, words with no vowels, etc. 

Let me know if you'd like me to explain any part of the solution or provide additional insight.