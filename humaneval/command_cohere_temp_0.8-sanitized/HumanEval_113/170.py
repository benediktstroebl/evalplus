def odd_count(strings):
    r = []
    for string in strings:
        odds = sum(1 for c in string if c % 2 == 1)
        r.append(f"the number of odd elements in the string {odds} of the input")
    return r