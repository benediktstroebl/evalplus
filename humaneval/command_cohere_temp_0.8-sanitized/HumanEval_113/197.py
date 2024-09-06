def odd_count(strings):
    r = []
    for string in strings:
        o = string.count('1') + string.count('3') + string.count('5')
        r.append(f"the number of odd elements in the string {string} of the input is: {o}")
    return r