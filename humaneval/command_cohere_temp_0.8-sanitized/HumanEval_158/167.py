def find_max(words):
    char_count = {}
    max_count = 0
    result = None
    for word in words:
        unique_chars = set(word)
        num_unique = len(unique_chars)
        if num_unique > max_count:
            max_count = num_unique
            result = word
        if num_unique == max_count:
            if word < result:
                result = word
    return result