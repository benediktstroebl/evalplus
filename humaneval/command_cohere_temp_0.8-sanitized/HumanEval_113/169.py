def odd_count(lst):
    r = []
    for num in lst:
        o = sum(1 for c in num if c % 2 != 0)
        r.append(f"the number of odd elements in the string {o} of the input")
    return r