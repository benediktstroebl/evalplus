def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(set(filter(lambda d: d % 2 == 0, digits))))
        r.append(f"the number of odd elements in the string {counts} of the input.")
    return r