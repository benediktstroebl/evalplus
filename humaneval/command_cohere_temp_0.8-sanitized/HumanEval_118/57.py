def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiouAEIOU'
    # O(n) time where n is the length of the word
    i = len(word) - 1
    while i >= 0 and word[i] not in vowels:
        if word[i] not in consonants:
            i -= 1
        else:
            j = i + 1
            while j < len(word) and word[j] not in vowels:
                if word[j] not in consonants:
                    j += 1
                else:
                    return word[i + 1:]
            i = j - 1
    return ''