def odd_count(lst):
    r = []
    for i, s in enumerate(lst, 1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input."
                 .replace(f'{i}', f"{n}"))
    return r