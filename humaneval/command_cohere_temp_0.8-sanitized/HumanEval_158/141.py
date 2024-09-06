def find_max(words):
    max_uniq = 0
    max_word = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            max_word = word
    return max_word