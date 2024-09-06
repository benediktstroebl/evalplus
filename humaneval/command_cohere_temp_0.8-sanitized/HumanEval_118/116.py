def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # Count index from right for each consonant and store the maximum
    max_consonant_index = max(list(word.lower()).index(c) for c in consonants if c in word)
    # Count index from right for each vowel and store the minimum
    min_vowel_index = min(list(word.lower()).index(v) for v in vowels if v in word and word[len(word) - len(v):].lower() != v)
    # Return the vowel that is closest to the maximum consonant index
    if min_vowel_index != -1 and max_consonant_index != len(word) - 1:
        return word[len(word) - min_vowel_index - 1 : len(word) - max_consonant_index - 1]
    else:
        return ""