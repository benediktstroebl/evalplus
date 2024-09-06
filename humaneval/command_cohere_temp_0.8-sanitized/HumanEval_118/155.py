def get_closest_vowel(word):
    """
    Finds the closest vowel to the right of a word, assuming the vowels occur between two consonants.
    Ignores starting and ending vowels.
    """
    # Ensure input is lowercase
    word = word.lower()
    # Split the word into onsets and rimes, using consonants as boundary
    word = word.split('con', n=1)
    if len(word) < 2:
        return ''
    
    # Handle cases with a single consonant and vowel or consonant only
    if len(word[0]) == 1:
        return word[1][0] if len(word[1]) > 0 else ''
    
    # Handle cases with double consonants
    if len(word[0]) > 2 and word[0][-2:] in 'ddggllmm':  # Double consonants
        return word[1][0] if len(word[1]) > 0 else ''
    
    # Handle cases with a long vowel sound
    if word[0].endswith('ee'):  # Long vowel sounds
        return word[0][-3:]
    
    # Find the index of the rightmost consonant in the onset
    idx = len(word[0]) - 1
    while word[0][idx] not in 'bcdfghjklmnpqrstvwxyz':
        idx -= 1
    idx += 1

    # Check if the consonant is doubled
    if idx < len(word[0]) - 1 and word[0][idx] == word[0][idx + 1]:
        idx += 1

    # Return the vowel if it occurs between two consonants, or an empty string
    return word[1][idx] if idx < len(word[1]) else ''