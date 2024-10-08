def find_max(words):
    max_unique = 0
    result = ""
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique or (unique_chars == max_unique and word < result):
            max_unique = unique_chars
            result = word
    return result
