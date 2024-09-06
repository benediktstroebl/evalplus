def odd_count(lst):
    r = []
    for idx, s in enumerate(lst):
        n = sum(1 for c in s if c % 2 == 1)
        r.append(f"the number of odd elements in the string {idx + 1} of the input is {n}")
    return r