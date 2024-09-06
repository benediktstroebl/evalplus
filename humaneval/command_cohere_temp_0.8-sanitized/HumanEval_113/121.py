def odd_count(strings):
    r = []
    for string in strings:
        counts = str(len(string) - sum(int(d) % 2 for d in string))
        r.append(f"the number of odd elements in the string {counts} of the input")
    return r