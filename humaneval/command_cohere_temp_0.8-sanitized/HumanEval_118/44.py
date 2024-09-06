def get_closest_vowel(word):
    cons_count = 0
    for char in word:
        if char.isalpha():
            if char.lower() in 'aeiou':
                vowel = True
            else:
                vowel = False
                if vowel:
                    cons_count = cons_count + 1
            if cons_count == 2 and vowel:
                return char
        else:
            cons_count = 0
    return ''