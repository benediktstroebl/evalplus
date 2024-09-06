def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, s))))
         for s in lst]
    return ["the number of odd elements " + str(i) + "n the str" + str(i) + "ng " + str(i) + " of the " + str(i) + "nput." for i in range(len(r))]