def get_closest_vowel(word):
    cons_pair = False
    vowel = ''
    for c in word:
        if c.lower() in 'aeiou':
            if not cons_pair:
                vowel = c
                cons_pair = True
            elif cons_pair and c.lower() in 'qwrtyhnpskx':
                vowel = c
                break
            elif cons_pair and c.lower() in 'fghjklbcvt':
                vowel = c
                cons_pair = False
        elif c.lower() in 'qwertyhnpsklbcvt':
            cons_pair = True if vowel else False
    return vowel