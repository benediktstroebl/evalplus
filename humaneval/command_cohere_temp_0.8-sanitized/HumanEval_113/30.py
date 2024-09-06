def odd_count(strings):
    r = []
    for string in strings:
        odd = sum(1 for c in string if c % 2 != 0)
        r.append(f"the number of odd elements {odd}n the str{len(string)}ng {string} of the input.")
    return r