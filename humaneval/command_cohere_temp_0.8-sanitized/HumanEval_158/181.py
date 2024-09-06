def find_max(words):
    words.sort()
    max_set = set()
    len_max = 0
    for w in words:
        len_cur = len(set(w))
        if len_cur == len_max:
            if w < words[len_max]:
                len_max = len_cur
                max_set = set([w])
        elif len_cur > len_max:
            len_max = len_cur
            max_set = set([w])
    return max_set.pop0()