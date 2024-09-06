def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {i} of the input is {n}")
    return r