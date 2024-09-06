def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    
    index = next((i for i, char in enumerate(word) if char in consonants), None)
    if index is None:
        return ''
    
    vowel = next((char for char in vowels if char in word[index:]), '')
    
    return vowel