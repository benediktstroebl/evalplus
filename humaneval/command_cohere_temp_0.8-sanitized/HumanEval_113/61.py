def odd_count(strings):
    lst = [str(len(list(filter(lambda d: d % 2 == 1, s)))) for s in strings]
    lst = ['the number of odd elements ' + f'in the string {i} of the input.' for i in lst]
    return lst