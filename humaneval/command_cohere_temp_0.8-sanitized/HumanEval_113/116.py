def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, d)))).replace('n', '{}'.format(i))
          for i, d in enumerate(lst)]
    return r