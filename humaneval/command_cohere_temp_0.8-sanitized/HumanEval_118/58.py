def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Remove starting and ending vowels
    word = word.strip(vowels)
    
    if not word:
        return ""

    # Find the first vowel between two consonants from the right
    for i in range(len(word)-1):
        if word[i] not in consonants and word[i+1] not in consonants and word[i+1] in vowels:
            return word[i+1]
    else:
        return ""