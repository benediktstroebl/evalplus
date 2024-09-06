def odd_count(lst):
    r = []
    for num in lst:
        counts = str(num).count('1')
        r.append(f'the number of odd elements in the string {num} of the input.' if counts == len(num) % 2 else f'{counts}n the string {num} of the input.')
    return r