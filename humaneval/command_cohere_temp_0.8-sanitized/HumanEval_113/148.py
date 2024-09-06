def odd_count(lst):
    r = []
    for s in lst:
        c = 0
        for c in s:
            if c % 2 != 0:
                c += 1
        r.append(f'the number of odd elements in the string {c} of the input.')
    return r