def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, s))))
         for s in lst]
    return ['the number of odd elements ' + ''.join(map(str, i)) + 'n the string ' + ''.join(map(str, s)) + ' of the input.'
            for i, s in enumerate(r)]