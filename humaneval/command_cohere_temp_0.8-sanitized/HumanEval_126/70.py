def is_sorted(lst):
    lst.sort()
    seen = set()
    for n in lst:
        if n in seen:
            return False
        seen.add(n)
    return True