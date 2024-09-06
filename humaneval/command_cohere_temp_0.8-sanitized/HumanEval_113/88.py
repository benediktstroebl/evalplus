def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(set(digits) & {x for x in digits if x % 2 == 0}))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r