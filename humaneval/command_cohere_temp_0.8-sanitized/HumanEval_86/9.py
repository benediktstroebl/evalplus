def anti_shuffle(s):
    word_inds = [i for i, char in enumerate(s) if char != " " and char != "]"]
    sorted_words = [chr(int(c)) for char in s for c in str(ord(char)-96)]
    return " ".join([s[i] for i in word_inds]+sorted_words)