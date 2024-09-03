def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    return word.isalpha(vowels[0]) and (word[-1] in vowels or word[-2] in vowels) and word[-1] in vowels and word[-2] in vowels