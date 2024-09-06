def get_closest_vowel(word):
    cons_idx = -1
    vowel = ""
    for i, char in enumerate(word):
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = char
                break
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                cons_idx = i
        elif char.isspace():
            if cons_idx != -1:
                vowel = word[cons_idx+1:]
                break
    return vowel