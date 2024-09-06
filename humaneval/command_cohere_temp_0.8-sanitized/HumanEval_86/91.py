def anti_shuffle(s):
    word_arr = []
    word = ""
    for c in s:
        if c == " ":
            if word:
                word_arr.append(word)
                word = ""
        else:
            word += c
    if word:
        word_arr.append(word)
    return " ".join(word_arr)