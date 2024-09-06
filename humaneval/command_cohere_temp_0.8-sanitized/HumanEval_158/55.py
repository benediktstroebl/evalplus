def find_max(words):
    words.sort()
    max_word = words[0]
    num_unique = len(set(max_word))
    for word in words:
        current_num_unique = len(set(word))
        if current_num_unique > num_unique:
            max_word = word
            num_unique = current_num_unique
    return max_word