def odd_count(lst):
    if len(lst) == 1:
        return [odd_count(lst)[0]]
    r = []
    for digits in lst:
        count = 0
        for d in digits:
            if d % 2:
                count += 1
        r.append(f"the number of odd elements in the string {count} of the input")
    return r