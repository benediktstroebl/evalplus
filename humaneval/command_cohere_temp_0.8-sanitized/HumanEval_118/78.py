def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qvwxz':
                cons_count += 1
        elif char.isspace():
            continue
        elif char.isdigit():
            if cons_count > 0:
                return char
        else:
            continue
    if cons_count > 0 and cons_count % 2 == 1:
        return char
    else:
        return ''