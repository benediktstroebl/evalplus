def select_words(s, n):
    if not s:
        return []
    return [word for word in s if word.count_consonant(word, n)]