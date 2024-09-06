def get_closest_vowel(word):
    cons = []
    vowel = ''
    word = word.lower()
    for c in word:
        if c in ['a', 'e', 'i', 'o', 'u']:
            if not cons or c != word[0] and c != word[-1]:
                vowel = c
        else:
            cons.append(c)
    return vowel