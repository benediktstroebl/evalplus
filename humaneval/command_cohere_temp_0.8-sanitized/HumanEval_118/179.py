def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
                if vowel:
                    cons_count += 1
        else:
            vowel = False

    if cons_count > 1:
        if vowel:
            return char.upper()
        else:
            return ''
    else:
        return ''