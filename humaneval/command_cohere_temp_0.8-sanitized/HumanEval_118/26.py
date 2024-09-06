def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    len_word = len(word)
    for i in range(len_word):
        if word[i] in vowels and word[i] == word[len_word - 1] and word[i] != word[len_word - 2]:
            return word[i]
    return ''