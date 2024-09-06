def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'

    # Extract substrings from the right, considering possible vowel placements
    right_consonants = [end for end in range(len(word) + 1 - 1)]
    while right_consonants[0] > 0 and word[right_consonants[0] - 1] not in vowels:
        right_consonants.pop(0)
    while right_consonants[-1] < len(word) and word[right_consonants[-1] + 1] not in vowels:
        right_consonants.pop()

    for vowel in vowels:
        if vowel in word:
            index = word.find(vowel)
            if index in right_consonants:
                return vowel
        elif index == 0 or index == len(word) or index == -1:
            continue
        else:
            for i in range(len(right_consonants)):
                if index + i >= 0 and index + i < len(word) and word[index + i] in consonants:
                    return vowel

    return ''