def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != ""]
    sorted_words = [chr(int(c)) for char in s for c in sorted(char)]
    return " ".join(sorted_words[i] if i in word_inds else " " for i in range(len(sorted_words)))