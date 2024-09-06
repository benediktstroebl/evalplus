def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in consonants and len_word - i - 1 >= 1 and word[len_word - i - 1] in consonants:
            for j in range(i + 1, len_word - i - 1):
                if word[j] in vowels:
                    return word[j]
    return ""