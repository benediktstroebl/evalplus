
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    if num < 0:
        return (-1, -1)
    elif num in [0, 1]:
        return (0, 0)
    elif num > 10:
        return (0, 0)
    else:
        ones = 0
        for i in range(1, len(str(num))):
            if str(num)[i] == '1':
                ones += 1
        return (ones, ones + 1)
