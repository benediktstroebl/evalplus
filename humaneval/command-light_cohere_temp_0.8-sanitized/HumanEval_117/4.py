def select_words(string, n):
    if not string:  # Empty string is valid input
        return []
    words = [word for word in string if word.count(word, n)]
    return words