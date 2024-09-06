def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    word = word.lower()
    index = next((i for i, let in enumerate(word) if let in consonants), len(word))
    if index == 0 or index == len(word) or word[index - 1:] == 'oa' or word[index - 1:] == 'ai':
        return ''
    return next((word[i] for i in range(index) if word[i] in vowels), '')