
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # a simple generator function which also yields the answer
    def iter_func(x, y):
        res = -1
        while (x < y):
            if x % 2 == 0:
                res = x
                x += 1
                yield res
            else:
                yield -1
                x += 1
                
    # function that returns the biggest even integer number inside the range
    def f(x, y):
        return max(filter(lambda x:x!=-1, iter_func(x, y)))

    # recursive function that returns the biggest even integer number inside the range
    def g(x, y):
        if x == y:
            return x
        elif x > y:
            return -1
        else:
            return f(x+1, y) if x % 2 == 0 else g(x+1, y)

    return g(min(x, y), max(x, y))

