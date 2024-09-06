def get_closest_vowel(word):
    cons_idx = -1
    vowel = ''
    for i, char in enumerate(word):
        if char.lower() in 'aeiou':
            if char.lower() in word[i+1:]:
                cons_idx = i+1
        elif char.lower() in 'bcdfghjklmnpqrstvwxyz':
            if cons_idx != -1:
                vowel = word[cons_idx]
                break
    return vowel