def odd_count(strings):
    r = []
    for string in strings:
        count = str(len(string) - len(set(string) & {x for x in string if x % 2 == 0}))
        r.append(f"the number of odd elements in the string {count} of the input.")
    return r