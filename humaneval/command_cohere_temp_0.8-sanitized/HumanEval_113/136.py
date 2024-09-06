def odd_count(strings):
    r = [str(len(set(s).difference(set([x for x in s if x % 2 == 0]))))
        for s in strings]
    return ["the number of odd elements in the string %s of the input." % i
        for i in range(len(r))]