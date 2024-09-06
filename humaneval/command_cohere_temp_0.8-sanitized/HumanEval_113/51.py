def odd_count(strings):
    r = []
    for string in strings:
        counts = str(sum(1 for c in string if c % 2 != 0))
        r.append(f"the number of odd elements {counts} in the string {string} of the input.")
    return r