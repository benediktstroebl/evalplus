def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # Finding possible positions for a vowel
    vowels_indices = [i for i, char in enumerate(word) if char in vowels]
    # Checking if the vowels are surrounded by consonants
    if len(word) == 1 or (len(word) >= 2 and vowels_indices[0] == 0 and vowels_indices[-1] == len(word) - 1):
        return ''

    for i in vowels_indices:
        left_consonant = word[i - 1] if i > 0 else word[i]
        right_consonant = word[i + 1] if i < len(word) - 1 else word[i]
        if left_consonant in consonants and right_consonant in consonants:
            return word[i]
    return ''