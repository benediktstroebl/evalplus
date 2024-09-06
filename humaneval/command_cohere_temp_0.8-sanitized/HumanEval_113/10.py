def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(1 for d in digits if d % 2 != 0)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r