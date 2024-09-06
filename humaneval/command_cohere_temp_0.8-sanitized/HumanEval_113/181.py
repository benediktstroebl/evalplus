def odd_count(lst):
    r = [str(len(re.findall(r'o(?)d\1', s))) for s in lst]
    r = ['the number of odd elements in the string ' + r.replace('o', '1') + ' of the input.']
    return r