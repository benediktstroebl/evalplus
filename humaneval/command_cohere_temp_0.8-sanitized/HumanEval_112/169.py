def reverse_delete(s, c):
    delete = [char for char in c]
    reverse = s[::-1]
    index = 0
    len_s = len(s)
    len_c = len(c)
    while index < len_s:
        if s[index] not in delete and reverse[index] not in delete:
            index += 1
        elif s[index] in delete and reverse[index] in delete:
            len_s -= 1
        else:
            index += 1
    if len_s <= 1:
        return s, False
    return s[:len_s], s[:len_s] == s[::-1]