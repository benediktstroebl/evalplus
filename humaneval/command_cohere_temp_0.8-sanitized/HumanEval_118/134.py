def get_closest_vowel(word):
    cons_pair = []
    right_index = 0
    for i, char in enumerate(word):
        if char.isalpha():
            if char.lower() in 'aeiou':
                if i > right_index and word[i-1].lower() not in 'aeiou':
                    right_index = i
            else:
                if i > right_index and word[i-1].lower() not in 'aeiou':
                    cons_pair.append(right_index)
                    right_index = i
    if right_index == 0:
        return ''
    prev_consonant = word[cons_pair[0] - 1] if cons_pair else word[right_index - 1]
    next_vowel = word[right_index] if right_index < len(word) - 1 and word[right_index + 1].lower() in 'aeiou' else ''
    if next_vowel == '' and word[right_index].lower() in 'aeiou':
        return word[right_index]
    if next_vowel == '' and word[right_index].lower() in 'ieou':
        if (prev_consonant in 'bcdfghjklmnpqrstvwxyz' and word[right_index].lower() in 'aeiou') or \
           (prev_consonant in 'aeioubcdfghjklmnpqrstvwxyz' and word[right_index].lower() in 'bcdfghjklmnpqrstvwxyz'):
            return word[right_index].upper()
        else:
            return word[right_index]
    return next_vowel