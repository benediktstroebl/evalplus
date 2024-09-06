def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel = 'aeiouAEIOU'
    res = ''
    for i in range(len(word)-1):
        if word[i] in vowel and word[i+1] in consonants and (res == '' or abs(vowel.find(res) - word[i] ) > abs(vowel.find(word[i]) - word[i+1])):
            res = word[i]
    return res