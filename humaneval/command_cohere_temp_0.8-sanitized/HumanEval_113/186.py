def odd_count(lst):
    r = []
    for i,n in enumerate(lst):
        d = ''.join(c if c % 2 else 'n' for c in n)
        r.append(f"the number of odd elements in the string {d} of the input.")
    return r