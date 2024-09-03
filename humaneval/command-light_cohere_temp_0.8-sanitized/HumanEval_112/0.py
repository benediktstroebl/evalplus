def reverse_delete(s, c):
    removed = set()
    for char in s:
        if char in c:
            removed.add(char)
    s = s.replace(char, "")
    if set(removed) == set(c):
        return (''.join(), True)
    return (''.join(), False)