def select_words(s, n):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    words = s.split()
    result = []
    word = ""
    for c in s:
        if c in consonants:
            if not word or c != " ":
                word += c
        else:
            if word == "":
                continue
            if len(word) == n:
                result.append(word)
                word = ""
    if word:
        result.append(word)
    if len(result) == 0:
        return [""]
    return result