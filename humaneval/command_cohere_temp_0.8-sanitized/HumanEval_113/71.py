def odd_count(strings):
    r = []
    for string in strings:
        # split string into list of digits
        d = list(string)
        # count odd digits
        n = sum(1 for x in d if x % 2 == 1)
        # format result
        r.append(f"the number of odd elements in the string {n} of the input.")
    return r