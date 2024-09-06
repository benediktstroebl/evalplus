def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != ""]
    sorted_letters = "".join(sorted(s, key=str.lower))
    return " ".join([s[i] for i in word_inds]) + " ".join(sorted_letters)