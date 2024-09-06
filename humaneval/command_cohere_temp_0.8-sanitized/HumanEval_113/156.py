def odd_count(lst):
    r = []
    for digits in lst:
        count = sum(int(d) % 2 for d in digits)
        r.append(f"the number of odd elements in the string {count} of the input")
    return r