def get_closest_vowel(word):
    cons_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for c in word:
        if c.lower() in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            if cons_count > 0:
                return c
        else:
            cons_count+=1
    return ''