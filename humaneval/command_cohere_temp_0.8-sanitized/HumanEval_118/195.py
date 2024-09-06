def get_closest_vowel(word):
    cons = []
    vowel = ""
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            if not cons or c.lower() != 'a':
                vowel = c
                cons = []
        elif c.isalpha():
            cons.append(c)
    return vowel