def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel:
                cons_count += 1
        else:
            continue
    if cons_count > 1:
        if word[-2].lower() in 'aeiou':
            return word[-2]
        elif word[-1].lower() in 'aeiou':
            return word[-1]
    return ''