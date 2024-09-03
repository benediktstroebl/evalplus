def get_closest_vowel(word):
    consonants = word[0:-1] + [word[-1]]
    vowels = "aeiouAEIOU"
    return vowels[min(consonants.index(c) -index(vowel) + 1) : len(vowels) - 1]