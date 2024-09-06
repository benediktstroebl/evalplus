def select_words(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        consonant_count = count_consonants(word)
        if len(consonant_count) == 1 and consonant_count[97] == n:
            result.append(word)
    return result