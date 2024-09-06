def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        r.append(f"the number of odd elements in the string {i} of the input.")
        r.append(f"{len([c for c in s if c % 2 == 1])}")
    return r