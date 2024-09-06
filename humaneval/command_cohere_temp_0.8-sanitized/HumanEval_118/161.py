def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming vowels at the start and end do not count.
    Empty string is returned if no such vowel exists.
    """
    # Ensure input is case-sensitive and only contains letters
    cleaned_word = ''.join(char.lower() for char in word if char.isalpha())
    if not cleaned_word:
        return ''
    
    # Use a dictionary to track last encountered consonant and vowel positions
    vowel_positions = {vowel: i for i, vowel in enumerate(cleaned_word) if vowel in 'AEIOUaeiou'}
    last_consonant = -1
    
    for i, char in enumerate(reversed(cleaned_word)):
        if char.isalpha() and char in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            last_consonant = i
    
    # Determine if a vowel was found between two consonants
    if last_consonant == -1:
        return cleaned_word[:1].upper() if cleaned_word else ''
    elif last_consonant + 1 >= len(cleaned_word) or cleaned_word[last_consonant + 1].isalpha():
        return ''
    else:
        closest_vowel = min(vowel_positions, key=lambda k: abs(last_consonant - vowel_positions[k]))
        return cleaned_word[vowel_positions[closest_vowel]].upper()