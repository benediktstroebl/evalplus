def sort_third(l: list):
    l_copy = l.copy()
    return [e if i % 3 != 0 else sorted(l_copy)[i // 3] for i, e in enumerate(l)]