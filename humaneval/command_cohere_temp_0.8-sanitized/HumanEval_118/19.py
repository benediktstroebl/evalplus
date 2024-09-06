def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    
    if len_word < 3:
        return ''

    # Find the first rightmost consonant
    for i in range(len_word):
        if word[i] in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            rightmost_consonant_index = i
            break

    # Find the closest vowel to the rightmost consonant
    for i in range(rightmost_consonant_index + 1, len_word):
        if word[i] in vowels:
            return word[i]
    return ''