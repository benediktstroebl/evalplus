def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Count the consonants and find the index of the last consonant
    consonant_count = word.lower().translate(str.maketrans('', '', consonants)).count( '')
    vowel_index = len(word) - consonant_count 
    # Check if a vowel is present at the calculated index to find the closest vowel
    if vowel_index < len(word) and word[vowel_index] in vowels:
        return word[vowel_index]
    else:
        return ''