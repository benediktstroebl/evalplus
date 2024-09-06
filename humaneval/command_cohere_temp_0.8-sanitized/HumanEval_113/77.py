def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, str(i)))))
         for i in lst]
    return ["the number of odd elements in the string %s of the input." % i
            for i in r]