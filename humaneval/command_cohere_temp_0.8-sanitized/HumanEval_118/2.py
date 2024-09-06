def get_closest_vowel(word):
    cons = []
    vowel = ""
    for c in word:
        if c.lower() in 'aeiou':
            if c.lower() in cons and not c.lower() == word[0]:
                vowel = c
        else:
            cons.append(c)
    return vowel