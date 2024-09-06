def find_max(words):
    words.sort()
    max_uniq = 0
    result = None
    for word in words:
        current_uniq = len(set(word))
        if current_uniq > max_uniq:
            max_uniq = current_uniq
            result = word
    return result