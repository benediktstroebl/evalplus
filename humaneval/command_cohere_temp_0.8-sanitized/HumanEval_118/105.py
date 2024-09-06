def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), len(word))
    if index == 0 or index == len(word) or word[index-1:] == 'an' or word[index-1:] == 'en':
        return ''
    
    vowel = next((v for v in vowels if v in word[index-2:index]), '')
    
    return vowel