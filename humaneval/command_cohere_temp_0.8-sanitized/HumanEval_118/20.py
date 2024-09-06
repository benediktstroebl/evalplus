def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'

    # Extract substrings from the right half that ends with a consonant
    right_halves = [substr for substr in word[1:]]
    for right_half in right_halves:
        if right_half.endswith(consonants):
            vowel = [c for c in right_half if c in vowels]
            if vowel:
                return vowel[0]
    return ""