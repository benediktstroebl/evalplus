def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # O(n) time where n is the length of the word
    for i in range(len(word)-1):
        if word[i] in consonants and word[i+1] in consonants:
            if word[i] in vowels or word[i+1] in vowels:
                return word[i] if word[i] in vowels else word[i+1]
    return ''