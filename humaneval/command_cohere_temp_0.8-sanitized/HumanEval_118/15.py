def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Extract substrings from the right side of the word until a consonant is met
    right_consonant_substrings = [substring for substring in word[1:] if substring[0] in consonants]
    
    # Find the closest vowel to the right side
    closest_vowel = next((sub for sub in right_consonant_substrings if sub.count(vowels) >= 1), '')

    # Check if the closest vowel is in the original word
    if closest_vowel and closest_vowel in word:
        return closest_vowel
    else:
        return ''