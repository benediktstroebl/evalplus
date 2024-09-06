def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        if char.isalpha():
            if char.lower() in vowels:
                if cons_count > 0:
                    return char
                else:
                    cons_count += 1
            else:
                cons_count += 1
        else:
            cons_count += 1
    return ''