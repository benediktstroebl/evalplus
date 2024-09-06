def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    len_word = len(word)

    for char in word:
        if char.isalpha():
            if char.lower() in vowels:
                if cons_count > 0:
                    return char
                else:
                    cons_count += 1
            elif char.lower() not in vowels:
                cons_count += 1
            else:
                # Count vowel in the beginning or ending as neither vowel nor consonant
                pass

    return ''