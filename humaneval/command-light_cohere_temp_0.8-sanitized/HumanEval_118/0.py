def get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for c in word[1:]:
        if c in vowels:
            return c
    return ""