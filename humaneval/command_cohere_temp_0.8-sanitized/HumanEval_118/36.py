def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Make sure the word contains at least 2 characters
    if len(word) < 2:
        return ''

    # Count leading and trailing vowels
    leading_vowels = sum(1 for char in word[:2] if char in vowels)
    trailing_vowels = sum(1 for char in word[-2:] if char in vowels)

    # Base case
    if leading_vowels + trailing_vowels == 2:
        return word[1] if word[1] in vowels else ''

    # Count the number of pairs of consonants in the word
    pairs = sum(1 for i in range(1, len(word) - 1) if word[i] in consonants and word[i + 1] in consonants)

    if pairs == 0:
        return ''

    # Find the index of the closest vowel to the last pair of consonants
    curr_distance = float('inf')
    vowel_index = 0
    for i in range(1, len(word) - 1):
        if word[i] in consonants and word[i + 1] in consonants:
            curr_distance = 1 + abs(i - (len(word) - 2))
        if word[i] in vowels:
            curr_distance = min(curr_distance, abs(i - (len(word) - 2)), abs(i - 1 - (len(word) - 2)))
        if curr_distance == 1:
            vowel_index = i
    return word[vowel_index] if vowel_index != 0 else ''