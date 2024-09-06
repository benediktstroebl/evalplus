def odd_count(lst):
    r = []
    for num in lst:
        count = 0
        for c in num:
            if c % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r