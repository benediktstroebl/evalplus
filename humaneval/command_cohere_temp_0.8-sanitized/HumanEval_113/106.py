def odd_count(lst):
    r = []
    for i, s in enumerate(lst, start=1):
        n = sum(int(d) % 2 == 1 for d in s)
        r.append(f"the number of odd elements in the string {i} of the input." if n == 1 else f"{n}n the string {i} of the input." )
    return r