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

    if cons_count < 2:
        return word[0].lower()

    right_index = len(word) - 1
    vowel_found = False
    for i in range(right_index):
        if word[i].lower() in 'aeiou':
            vowel_found = True
            break

    if not vowel_found:
        return ''

    return word[i].lower()