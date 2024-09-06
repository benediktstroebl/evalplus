def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, s))))
         for s in lst]
    return ["the number of odd elements " + r[i] + " the string " + str(i) + " of the input."
            for i in range(len(r))]