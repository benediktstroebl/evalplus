def odd_count(lst):
    r = []
    for num in lst:
        c = 0
        for d in num:
            if d % 2:
                c += 1
        r.append(f"the number of odd elements in the string {c} of the input")
    return r