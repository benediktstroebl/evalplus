def find_max(words):
    max_unique_words = sorted(words, key=lambda word: (len(set(word)), word))
    return max_unique_words[0]