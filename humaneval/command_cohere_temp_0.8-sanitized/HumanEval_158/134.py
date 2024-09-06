def find_max(words):
    words.sort()
    max_set = set()
    len_max = 0
    for word in words:
        len_cur = len(set(word))
        if len_cur == len_max:
            if word < words[len_max]:
                len_max = len_cur
                max_set = set([word])
        elif len_cur > len_max:
            len_max = len_cur
            max_set = set([word])
    return max_set.pop0()