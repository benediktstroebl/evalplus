def odd_count(strings):
    r = []
    for string in strings:
        # strip any non-digit characters from the input
        string = str(eval(string))
        count = len(string) - string.count('0') - string.count('7') - string.count('4')
        r.append(f"the number of odd elements in the string {count} of the input.")
    return r