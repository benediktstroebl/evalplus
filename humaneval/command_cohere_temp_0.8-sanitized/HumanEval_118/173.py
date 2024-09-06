def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # O(n) time, where n is the length of the word
    for i in range(len(word)-1):
        if word[i] in vowels and word[i+1] in consonants:
            return word[i]
    return ''