def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qu':
                cons_count += 1
        else:
            continue
    if cons_count > 1:
        for char in word[::-1]:
            if char.isalpha():
                if char.lower() in 'aeiou':
                    return char
                elif char.lower() not in 'qu':
                    cons_count -= 1
                    if cons_count == 1:
                        return char
    return ''