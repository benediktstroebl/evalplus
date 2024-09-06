def odd_count(strings):
    lst = [str(len(set(s)) - len(set(s)[::2])) for s in strings]
    lst = ['the number of odd elements ' + i + ' in the string ' + i + ' of the input.' for i in lst]
    return lst