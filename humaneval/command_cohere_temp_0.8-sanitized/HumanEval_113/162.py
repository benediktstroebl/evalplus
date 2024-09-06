def odd_count(lst):
    r = []
    for num in lst:
        counts = str(num).count('1')
        r.append(f'the number of odd elements in the string {counts} of the input.')
    return r