def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(sum(1 for c in digits if c % 2 != 0))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r