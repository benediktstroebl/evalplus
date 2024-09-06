def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'bcdfghjklmnpqrstvwxyz':
                cons_count += 1
            elif char.lower() in 'aeiou':
                if cons_count > 0:
                    return char
                cons_count = 0
    return ''