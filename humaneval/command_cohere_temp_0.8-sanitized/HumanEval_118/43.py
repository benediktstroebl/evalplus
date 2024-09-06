def get_closest_vowel(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowels = 'aeiouAEIOU'
    # Count the leading and trailing consonants
    start, end = 0, len(word) - 1
    while start < end and word[start] not in vowels:
        start += 1
    while end > start and word[end] not in vowels:
        end -= 1
    # Count the consecutive consonants
    count = end - start - 1
    if count == 0:
        return word[start:] if start < end else ''
    # Find the vowel closer to the middle
    for i in range(start, end):
        if word[i] in vowels:
            if i - start < end - i:
                return word[i:] if start < end else word[:i]
            else:
                return word[i:] if start < end else word[:i]
    return ''