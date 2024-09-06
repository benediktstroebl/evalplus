def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != ""]
    sorted_words = [chr(int(char)) for char in sorted(s[i] for i in word_inds)]
    return " ".join(sorted_words)