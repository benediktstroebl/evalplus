def odd_count(lst):
    r = []
    for digits in lst:
        counts = str(len(set(digits)) - len(digits) // 2)
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r