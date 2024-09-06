def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'bcdfghjklmnpqrstvwxyz':
                cons_count += 1
        elif char.isspace():
            continue
        elif char == '-':
            continue
        else:
            return ''
    if cons_count > 1:
        if word[-2].lower() in 'aeiou':
            return word[-2]
    return ''