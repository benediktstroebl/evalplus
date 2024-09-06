def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    index = len(word) - 1
    while index >= 0 and word[index] in consonants:
        index -= 1
    if index == -1:
        return ''
    left_consonant = word[index]
    right_consonant = word[index + 1]
    for vowel in vowels:
        if vowel == left_consonant or vowel == right_consonant:
            return vowel
    return vowels[vowels.find(left_consonant) // 2 + vowels.find(right_consonant) // 2]