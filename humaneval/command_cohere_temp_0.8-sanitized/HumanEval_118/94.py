def get_closest_vowel(word):
    cons = []
    for c in word:
        if c.lower() not in 'aeuio':
            cons.append(c)
    left, right = 0, len(word) - 1
    if len(cons) < 2:
        return ''

    while left + 1 < right and cons[left] == cons[right]:
        left += 1
    while left - 1 >= 0 and cons[left] == cons[right]:
        right -= 1

    if left == right:
        return ''

    vowels = ['a', 'e', 'i', 'o', 'u']
    for v in vowels:
        if v in cons[left:right+1]:
            return v

    return ''