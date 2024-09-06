def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    
    # Extract substrings after the last consonant and before the first vowel from the end
    for last_consonant_idx in range(len(word) - 2, -1, -1):
        if word[last_consonant_idx] not in consonants:
            continue
        substring = word[last_consonant_idx + 1:]
        if any(char in vowel for char in substring):
            return substring[::-1][0] if substring else ''

    # If no matching vowel found from the previous logic, try the whole word
    if any(char in vowel for char in word):
        return word
    
    return ''