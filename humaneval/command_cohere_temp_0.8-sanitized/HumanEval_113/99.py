def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, d)))) for d in lst]
    return ['the number of odd elements ' + ''.join(map(str, i)) + ' in the string ' + ''.join(map(str, j)) + ' of the input' for i, j in zip(r, lst)]