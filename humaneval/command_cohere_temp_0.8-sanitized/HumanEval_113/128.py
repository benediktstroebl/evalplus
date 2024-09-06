def odd_count(lst):
    r = []
    for num in lst:
        a = str(num)
        b = 0
        for x in a:
            if int(x) % 2:
                b += 1
        r.append(f"the number of odd elements in the string {b} of the input.")
    return r