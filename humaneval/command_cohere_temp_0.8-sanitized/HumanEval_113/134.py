def odd_count(strings):
    res = [str(len(set(s).difference(set([0, 2, 4, 6, 8]))))
           for s in strings]
    return ["the number of odd elements " + i + "n the string " + str(j) + " of the input."
            for i, j in zip(res, strings)]