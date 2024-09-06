def monotonic(lst):
    if len(lst) < 2:
        return True
    a = lst[0]
    for b in lst[1:]:
        if a > b and a != b or a < b and a != b:
            return False
        a = b
    return True