def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, num)))).replace('n', str(i))
          for i, num in enumerate(lst)]
    return r