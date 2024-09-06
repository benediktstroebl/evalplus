def odd_count(lst):
    r = [str(len(list(filter(lambda d: d % 2 == 1, s))))
         for s in lst]
    return ["the number of odd elements " + str(i) + "n the string " + str(i) + " of the input."
            for i in range(len(r))]