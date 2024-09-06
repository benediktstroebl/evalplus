def odd_count(strings):
    res = [str(len(list(filter(lambda x: x % 2 == 1, s))))
           for s in strings]
    return ["the number of odd elements " + str(i) + "n the string " + str(i) + " of the input."
            for i in res]