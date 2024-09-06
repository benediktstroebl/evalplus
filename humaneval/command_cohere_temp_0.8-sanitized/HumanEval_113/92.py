def odd_count(lst):
    r = []
    for num in lst:
        o = sum(1 for c in num if c % 2 != 0)
        r += [f"the number of odd elements {o} in the string {num} of the input"]
    return r