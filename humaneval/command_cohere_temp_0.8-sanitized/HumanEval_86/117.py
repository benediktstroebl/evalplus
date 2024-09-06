def anti_shuffle(s):
    word_starts = [i for i, char in enumerate(s) if char != " " and char != " "]
    sorted_words = [chr(int(c)) for char in s for c in sorted(char)]
    return " ".join(sorted_words[start:stop] for start, stop in zip(word_starts, word_starts[1:]))