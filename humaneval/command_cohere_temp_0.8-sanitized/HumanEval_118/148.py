def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    word = word.upper()
    
    if not word.startswith(consonants) or not word.endswith(consonants):
        return word[0] if word[1:].count(consonants) == word[1:].count(vowels) else word[1:]
    
    index = -1
    for i in range(1, len(word) - 1):
        if word[i] in vowels:
            index = i
            break

    return word[index + 1] if index != -1 else ''