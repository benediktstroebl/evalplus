def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
            if not vowel and char.lower() not in 'qwerty':
                cons_count += 1
        else:
            continue
    
    if cons_count > 1:
        if word[-2].lower() in 'aeiou':
            return word[-2]
    elif cons_count == 1:
        if word[-1].lower() in 'aeiou':
            return word[-1]
    return ''