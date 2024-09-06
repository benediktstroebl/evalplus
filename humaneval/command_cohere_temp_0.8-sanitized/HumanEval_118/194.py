def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    # Removing the first and last character to neglect vowels at the beginning and ending.
    stripped_word = word[1:-1]
    # Splitting the remaining string into pairs of adjacent characters.
    pairs = stripped_word.split('')
    # Filtering out pairs that consist of two consonants.
    qualified_pairs = [pair for pair in pairs if pair not in consonants * 2]
    
    # If there are qualifying pairs, return the vowel directly between them.
    if qualified_pairs:
        return vowels[qualified_pairs.index(consonants * 2)]
    # If no qualifying pairs, return an empty string.
    else:
        return ''