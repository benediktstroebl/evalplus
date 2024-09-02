
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, 1)
    else:
        if num == 0:
            return (0, 0)
        elif num < 10:
            return (num, 0)
        else:
            i = 1
            while True:
                if num % 10 == i:
                    break
                i += 1
            return (num // i, 1)
