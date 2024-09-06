def odd_count(strings):
    r = [str(len(set(s).difference(list(range(0, 10, 2))))
           or '0') + 'n the str' + str(i+1) + 'ng ' + str(i+1) + ' of the '
         + 'input.' for i, s in enumerate(strings, 1)]
    return r